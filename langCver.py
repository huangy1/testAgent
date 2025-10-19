# main.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import tools_2

# 加载环境变量
load_dotenv()

# 初始化模型
llm = ChatOpenAI(
    model="qwen-flash",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    temperature=0.7
)

# 加载工具
tools_list = [tools_2.read_file, tools_2.list_files, tools_2.rename_file]

# 定义提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced programmer. Use tools when needed."),
    MessagesPlaceholder(variable_name="chat_history"),  # 对话历史占位符
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # 工具调用中间步骤
])

# 创建记忆（对话历史）
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 创建 Agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools_list,
    prompt=prompt
)

# 创建 Agent 执行器
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools_list,
    memory=memory,
    verbose=True  # 打印思考过程
)


def main():
    print("Agent is running. Type 'exit' to quit.\n")
    while True:
        user_input = input("Input: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if not user_input:
            continue

        try:
            # 执行 Agent
            response = agent_executor.invoke({"input": user_input})
            print(f"Assistant: {response['output']}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()