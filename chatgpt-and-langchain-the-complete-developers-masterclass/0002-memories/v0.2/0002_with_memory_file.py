from dotenv import load_dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

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
chain = prompt_template | model
config = {
    "configurable": {
        "session_id": "001"
    }
}


# ---------- Memory ----------
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = FileChatMessageHistory('messages.json')
    return store[session_id]

# ---------- / Memory ----------


# ---------- App ----------
app = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="messages",
)
# ---------- / App ----------


# ---------- Start ----------
while True:
    content = input(">> ")
    response = app.invoke(
        {
            "messages": [HumanMessage(content=content)],
            "language": "Indonesian"
        },
        config=config,
    )
    print(response.content)
# ---------- / Start ----------
