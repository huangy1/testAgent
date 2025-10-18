# main.py
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os
import tools_2

# 加载环境变量
load_dotenv()

# 初始化模型（使用 DashScope 的 OpenAI 兼容接口）
llm = ChatOpenAI(
    model="qwen-flash",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    temperature=0.7
)

# 绑定工具
tools_list = [tools_2.read_file, tools_2.list_files, tools_2.rename_file]
llm_with_tools = llm.bind_tools(tools_list)

# 定义系统提示
system_message = SystemMessage(content="You are an experienced programmer. Use tools when needed.")

# 构建状态图（基于 MessagesState）
class AgentState(MessagesState):
    pass

graph_builder = StateGraph(AgentState)

# 工具节点
tool_node = ToolNode(tools_list)

# Agent 节点（决策者）
def agent_node(state: AgentState):
    messages = [system_message] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# 添加节点
graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)

# 设置入口
graph_builder.set_entry_point("agent")

# 使用 tools_condition 判断是否需要调用工具
graph_builder.add_conditional_edges(
    "agent",
    tools_condition,  # 自动判断是否调用工具
)
graph_builder.add_edge("tools", "agent")  # 工具执行后回到 agent

# 启用内存（对话历史）
memory = MemorySaver()
app = graph_builder.compile(checkpointer=memory)


def main():
    config = {"configurable": {"thread_id": "1"}}  # 会话 ID

    print("Agent is running. Type 'exit' to quit.")
    while True:
        user_input = input("\nInput: ")
        if user_input.lower() == "exit":
            break

        # 发送消息并流式输出
        events = app.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config=config,
            stream_mode="values"
        )
        for event in events:
            if "messages" in event:
                last_message = event["messages"][-1]
                if not isinstance(last_message, HumanMessage):
                    print(f"Assistant: {last_message.content}")

if __name__ == "__main__":
    main()