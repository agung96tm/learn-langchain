from typing import TypedDict, Annotated, Sequence

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph, add_messages
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
config = {"configurable": {"thread_id": "001"}}


# ---------- Memory ----------
memory = MemorySaver()

# ---------- / Memory ----------


# ---------- App ----------
class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str


workflow = StateGraph(state_schema=State)


def call_model(state: State):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": [response]}


workflow.add_edge(START, "model")
workflow.add_node("model", call_model)
app = workflow.compile(checkpointer=memory)

# ---------- /App ----------


# ---------- Start ----------
while True:
    content = input(">> ")
    output = app.invoke(
        {
            "messages": [HumanMessage(content)],
            "language": "Indonesian",
        },
        config=config,
    )
    print(output['messages'][-1].content)
# ---------- /Start ----------
