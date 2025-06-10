from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

#aqui eu carrego o doc
loader = TextLoader("./doc/exemplo.txt")
documents = loader.load()

#divide o texto em pedaços
TextLoader_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = TextLoader_splitter.split_documents(documents)

#trabalhar com embeddings E BANCO DE DADOS
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

chain = load_qa_chain(llm, chain_type="stuff")

while True:
    pergunta = input("Digite sua pergunta sobre o documento(Ou 'sair' para encerrar): ")
    if pergunta.lower() == 'sair':
        break
    docs_relevantes = db.similarity_search(pergunta)
    resposta = chain.run(input_documents=docs_relevantes, question=pergunta)
    print("\nResposta: ", resposta)   



docs_relevantes = db.similarity_search(pergunta)



resposta = chain.run(input_documents=docs_relevantes, question=pergunta)

print("\nResposta: ", resposta)


