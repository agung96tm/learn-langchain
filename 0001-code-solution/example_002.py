from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


# Example 2
# The purpose of this code is to use the LangChain library to generate a Python function based on a specified task.
# It loads environment variables, initializes the necessary components,
# creates a prompt template for generating the code, and
# then invokes the OpenAI model to produce a short Python function that returns a list of numbers.
# Finally, it formats and prints the generated code.

# Run:
# >> python example_002.py

#
load_dotenv()

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
    "language": "python",
    "task": "return a list of numbers"
})

#
print(printable)
