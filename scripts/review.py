import subprocess
import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def getDiff():
    return subprocess.check_output(['git', 'show'], text=True)


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

def main():
    diff = getDiff()
    
    prompt = f"Review the following code changes and provide feedback:\n\n{diff}\n\nMandatory: Provie output in HTML formate that can use to sent in mail"
    response = llm.invoke(prompt)
    print("Code Review Feedback: ")
    print(response.text)
    
main()