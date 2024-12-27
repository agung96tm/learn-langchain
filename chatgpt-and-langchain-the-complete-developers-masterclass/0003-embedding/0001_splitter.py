from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0,
)

loader = TextLoader('./facts.txt')
docs = loader.load_and_split(text_splitter=text_splitter)

for doc in docs:
    print(doc)
    print("-----")
