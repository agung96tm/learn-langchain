from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


parser = StrOutputParser()
model = ChatOpenAI()
messages = [
    HumanMessage(content="give me indonesian joke"),
]

result = model.invoke(messages)
printable = parser.invoke(result)

print(printable)
