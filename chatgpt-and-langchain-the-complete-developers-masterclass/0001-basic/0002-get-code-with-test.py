from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Code(BaseModel):
    code: str = Field()
    test: str = Field()


model = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages([
    ('user', "Write a very short {language} function that {task}, provide test function too")
])
chain = prompt | model.with_structured_output(Code)

result: Code = chain.invoke({
    "language": "python",
    "task": "return list of numbers",
})

print("---- Code ----")
print(result.code)
print("---- Test ----")
print(result.test)
