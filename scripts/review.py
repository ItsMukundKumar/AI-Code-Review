import subprocess
import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def getDiff():
    return subprocess.check_output(['git', 'show'], text=True)


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

output = llm.invoke('Hello!')


print(output.content)