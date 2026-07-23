import subprocess
import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()


def getDiff():
    return subprocess.check_output(["git", "show"], text=True)


llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


def send_email(html_content):
    msg = EmailMessage()
    msg["Subject"] = "Code Review Feedback"
    msg["From"] = "shahmukund060@gmail.com"
    msg["to"] = "mukundkumarshah93@gmail.com"
    msg.set_content("Please find the codereview feedback below.")
    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 456) as smtp:
        smtp.login("shahmukund060@gmail.com", os.getenv("MAIL_APP_PASSWORD"))  # type: ignore
        smtp.send_message(msg)
        
    
    print('Email sent Successfully')


def main():
    diff = getDiff()

    prompt = f"Review the following code changes and provide feedback:\n\nMandatory: Provie output in HTML that can use to sent in mail\n\n{diff}"
    response = llm.invoke(prompt)

    html_content = response.text
    
    send_email(html_content)

main()
