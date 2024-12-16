from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()
prompt = ChatPromptTemplate.from_messages([
    ('user', "Write a very short {language} function that {task}")
])
parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({
    "language": "python",
    "task": "return list of numbers",
})

print(result)
