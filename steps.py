#primeira parte
#usar o ollama para realizar um chat
'''
import ollama

while True:
	print("")
	formatted_prompt = input('Faça uma pergunta: ')
	result = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
	print(result['message']['content'])
'''
#segunda parte
# usar o langchain
#https://python.langchain.com/docs/guides/development/local_llms/
'''
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
while True:
	formatted_prompt = input('Faça uma pergunta: ')
	print(llm.invoke(formatted_prompt))
'''
#terceira parte
# usar o langchain com respostas em stream
'''
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(
    model="llama2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)
while True:
	formatted_prompt = input('Faça uma pergunta: ')
	print(llm.invoke(formatted_prompt))
'''

#quarta parte
#https://python.langchain.com/docs/integrations/document_loaders/web_base/
#https://python.langchain.com/docs/modules/data_connection/retrievers/vectorstore/
'''
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

import ollama

def load_and_retrieve_docs(url):
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict() 
    )
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,
    	chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":2})

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def rag_chain(url, question):
    retriever = load_and_retrieve_docs(url)
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']

url = "https://github.com/mvdiogo/CrewAI"
question = "Como instalar o crewai"
result = rag_chain(url, question)

print(result)
'''

#quinta parte
#multiplas pesquisas em um texto
'''
from langchain_community.retrievers import BM25Retriever

nome_arquivo = "quemmatouodete.txt"
with open(nome_arquivo, 'r') as arquivo:
    linhas = [linha.strip() for linha in arquivo.readlines()]

retriever = BM25Retriever.from_texts(linhas, similarity_top_k=5)

result = retriever.invoke("quem matou odete roitman")

print(result)
'''

#sexta parte
'''
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

params = {"lang":"pt","top_k_results":5}
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(params = params))

result = wikipedia.run("coronel silvino")
print(result)
'''
#setima parte
'''
import wikipedia
wikipedia.set_lang('pt')
result = wikipedia.summary('Coronel Silvino', sentences = 10, auto_suggest = True)
#result = wikipedia.search('Coronel silvino')
print(result)
'''
#oitava parte
#https://python.langchain.com/docs/integrations/tools/ddg/
'''
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

search = DuckDuckGoSearchResults()
wrapper = DuckDuckGoSearchAPIWrapper(region="pt-br", time="d", max_results=10)
search = DuckDuckGoSearchResults(api_wrapper=wrapper)

print(search.run("flisol"))
'''
#nova parte
#https://python.langchain.com/docs/integrations/document_loaders/image_captions/
'''
from langchain_community.document_loaders.image import UnstructuredImageLoader
from langchain_community.document_loaders import ImageCaptionLoader
loader = UnstructuredImageLoader("1.png")
data = loader.load()
print(data)

loader = ImageCaptionLoader('ogaroto.jpg')
doc = loader.load()
print(doc)
'''

