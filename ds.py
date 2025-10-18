import openai
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel, OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import tools
from dotenv import load_dotenv
import os # 添加os模块用于加载环境变量
load_dotenv()
# 修正模型配置

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

# client = openai.OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url=os.getenv("DEEPSEEK_BASE_URL")
# )

# model = OpenAIModel("deepseek-chat",provider=OpenAIProvider(api_key=api_key, base_url=base_url))
model = OpenAIChatModel("deepseek-reasoner",provider=OpenAIProvider(api_key=api_key, base_url=base_url))
agent = Agent(model,system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main():
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)


if __name__ == "__main__":
    main()

