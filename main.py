from langchain_documents_loader import TextLoader
from langchain.text_splitter import CaracterTextSplitter
from lanchain.vectorstores import FAISS
from lanchain.embeddings import OpenAIEmbeddings
from langchain.questions_answering import load_qa_chain
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

