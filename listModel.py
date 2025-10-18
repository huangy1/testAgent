import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# 确保你的 API 密钥已正确设置为环境变量
# 或者你可以直接在这里赋值：genai.configure(api_key="YOUR_API_KEY")
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

print("可用模型列表:")
for m in genai.list_models():
    # 筛选出支持 generateContent 方法的模型
    if 'generateContent' in m.supported_generation_methods:
        print(f"  - {m.name}")