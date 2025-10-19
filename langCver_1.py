# main.py
# 包含记忆的版本
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage
# 注意新的导入路径
from langchain.agents import create_agent#, agent_executor
from langgraph.checkpoint.memory import InMemorySaver
# from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import tools_2

# 加载环境变量
load_dotenv()

# 初始化模型 - 这部分通常无需改动
llm = ChatOpenAI(
    model="qwen-flash",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    temperature=0.7
)

# 加载工具
tools_list = [tools_2.read_file, tools_2.list_files, tools_2.rename_file]

# 定义提示词模板 - 注意变量的命名可能需参照新版本
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced programmer. Use tools when needed."),
    MessagesPlaceholder(variable_name="messages"),  # 变量名可能改为 "messages"
    ("human", "{input}"),
    # Agent scratchpad 的处理方式在新版本中可能有变
])

# 内存（对话历史） - 在新版本中，内存管理方式有变，更推荐与LangGraph结合使用 :cite[7]
# 对于简单测试，可先尝试保留，但注意其与代理的兼容性
# memory = ConversationBufferMemory(
#     memory_key="chat_history",
#     return_messages=True
# )

# 创建 Agent - 这是核心变更点
# 使用新的 create_agent 函数 :cite[1]
agent = create_agent(
    model=llm,
    tools=tools_list,
    system_prompt="You are an experienced programmer. Use tools when needed.",  # 确认参数名是否仍为 `prompt`，或已改为 `system_prompt`
    checkpointer=InMemorySaver(),
)

# 创建 Agent 执行器 - 使用新的 agent_executor 函数 :cite[1]
# executor = agent_executor(
#     agent=agent,
#     tools=tools_list,
#     memory=memory,  # 检查新执行器是否仍支持 memory 参数
#     verbose=True
# )

def print_response(response):
    """提取并打印最终AI回复"""
    if isinstance(response, dict) and 'messages' in response:
        messages = response['messages']
        # 找到最后一个AIMessage
        for message in reversed(messages):
            if hasattr(message, 'content') and message.content and not hasattr(message, 'tool_calls'):
                print(f"Assistant: {message.content}\n")
                return
    print(f"Assistant: {response}\n")


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
            # 调用执行器 - 输入格式可能发生变化
            # response = agent.invoke({"input": user_input})
            response = agent.invoke({"messages": [{"role": "user", "content": user_input}]},
                                    {"configurable": {"thread_id": "1"}})
            print(response)
            # print_response(response)
            # response = agent.invoke({"input": user_input},
            #                         {"configurable": {"thread_id": "1"}})
            # print(response)
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()