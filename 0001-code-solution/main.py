from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

#
parser = StrOutputParser()
model = ChatOpenAI()
prompt_template = ChatPromptTemplate.from_messages([
    ("user", "Write a very sort {language} function that will {task}"),
])

#
chain = prompt_template | model | parser
printable = chain.invoke({
    "language": "python",
    "task": "return a list of numbers"
})

#
print(printable)
