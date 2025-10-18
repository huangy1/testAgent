from pydantic_ai.models.google import GoogleModel
from pydantic_ai import Agent

from dotenv import load_dotenv
import tools


load_dotenv()
# model = GoogleModel("gemini-1.5-flash-latest")
model = GoogleModel("gemini-2.5-flash")
agent = Agent(model,
              system_prompt="You are an experienced programmer",
            #   tools=[tools.read_file, tools.list_files, tools.rename_file])
            tools=[tools.read_file, tools.list_files])

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

