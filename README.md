. : 无法加载文件 C:\Users\16272\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参
阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3
+ . 'C:\Users\16272\Documents\WindowsPowerShell\profile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
#第一次设置conda报错（win powershell中）


test prompt:list and read file, base on your knowledge, tell me what lang each file use.

file:///C:/path/to/image.jpg #background 图片设置路径

form . import tools #__init__.py 需要

已追踪文件加入ignore,先
```bash
git rm --cached .env  
```
deepseek不支持openai的response API，所以用不了OpenAIResponsesModel

使用消息格式
```python
from langchain_core.messages import HumanMessage, SystemMessage

# 使用消息格式
messages = [
    SystemMessage(content="你是一个专业的编程助手。"),
    HumanMessage(content="请帮我写一个Python函数来计算斐波那契数列。")
]

response = llm.invoke(messages)
print(response.content)
```
加入prompt模版
```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# 定义prompt模板
text = """
你是一个专业的编程助手。请根据以下上下文信息回答问题：

上下文信息：
{context}

用户问题：{question}

请基于上下文信息提供准确的回答。
"""

# 创建prompt模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的编程助手。"),
    ("human", text)
])

# 准备上下文和问题
context = """
Python是一种高级编程语言，具有简洁的语法和强大的功能。
斐波那契数列是一个经典的数学问题，每个数字是前两个数字的和。
"""

question = "请帮我写一个Python函数来计算斐波那契数列。"

# 格式化prompt模板
formatted_prompt = prompt_template.format(
    context=context,
    question=question
)

# 调用模型
response = llm.invoke(formatted_prompt)
print(response.content)
```