# from google import genai
# from dotenv import load_dotenv

# load_dotenv()

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)


from google import generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# 配置 API 密钥
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# 创建一个模型实例
model = genai.GenerativeModel("gemini-1.5-flash")

# 使用模型实例生成内容
response = model.generate_content("用几句话解释人工智能是如何工作的")

# 打印响应文本
print(response.text)

