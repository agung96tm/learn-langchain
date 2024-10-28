from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


# Example 1
# The purpose of this code is to generate a code snippet based on user-defined tasks and programming languages.
# It loads environment variables, accepts command-line arguments for the task and language,
# constructs a prompt to instruct the OpenAI model to create a function,
# and finally invokes the model to print the generated code.

# Run:
# >> python example_001.py

#
load_dotenv()

#
output_parser = StrOutputParser()
model = ChatOpenAI()
messages = [
    HumanMessage(content="give me indonesian joke"),
]

#
result = model.invoke(messages)
printable = output_parser.invoke(result)

#
print(printable)
