from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import argparse
from pydantic import BaseModel


# Example 4
# The purpose of this code is to generate a code snippet and its corresponding test
# based on user-defined tasks and programming languages. It loads environment variables,
# accepts command-line arguments for the task and language, constructs prompts for
# generating the function and its test, and finally invokes the OpenAI model to print
# both the generated code and test.

# Run:
# >> python example_004.py
# >> python example_004.py --task="return modulus 2" --language="javascript"

#
load_dotenv()

#
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

#
output_parser = StrOutputParser()
model = ChatOpenAI()

#
code_template = ChatPromptTemplate.from_messages([
    ("user", "Write a very sort {language} function that will {task}"),
])
test_template = ChatPromptTemplate.from_messages([
    ("user", "Write a test for the following {language} code: {code}")
])


#
class CodeSchema(BaseModel):
    code: str
    test: str


#
chain = (
    # code
    (code_template | model | output_parser)

    # test
    | (lambda i: {"language": args.language, "code": i})
    | test_template | model.with_structured_output(CodeSchema)
)

#
printable = chain.invoke({"language": args.language, "task": args.task})

print(">>>> GENERATED CODE:")
print(printable.code)
print("")

print(">>>> GENERATED TEST:")
print(printable.test)
