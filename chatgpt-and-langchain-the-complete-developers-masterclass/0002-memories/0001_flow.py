from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

result = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)
print(result)
