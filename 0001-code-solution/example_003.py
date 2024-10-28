from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import argparse


# Example 3
# The purpose of this code is to generate a code snippet based on user-defined tasks and programming languages.
# It loads environment variables, accepts command-line arguments for the task and language,
# and constructs a prompt to instruct the OpenAI model to create a function.
# Finally, it invokes the model and prints the generated code.

# Run:
# >> python example_003.py
# >> python example_003.py --task="return modulus 2" --language="javascript"

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
code_template = ChatPromptTemplate.from_messages([
    ("user", "Write a very sort {language} function that will {task}"),
])

#
chain = code_template | model | output_parser

#
printable = chain.invoke({
    "language": args.language,
    "task": args.task
})

#
print(printable)
