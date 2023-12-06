import gradio as gr
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer,util
import numpy as np
import faiss
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import dotenv
import os
from langchain import OpenAI

dotenv.load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def semantic_search(Question, *urls):
    urls = [url for url in urls if url]
    loader = UnstructuredURLLoader(urls=list(urls))
    data=loader.load()
    text_splitter = RecursiveCharacterTextSplitter(separators='\n',chunk_size=600,chunk_overlap=100)
    docs=text_splitter.split_documents(data)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    docc=[]
    metadata=[]
    for i in range(len(docs)):
        docc.append(docs[i].page_content)
        metadata.append(docs[i].metadata)
    embed=model.encode(docc)
    dim=embed.shape[1]
    index=faiss.IndexFlatL2(dim)
    index.add(embed)
    index_filename = 'index_flat_l2.index'
    faiss.write_index(index, index_filename)
    index_filename = 'index_flat_l2.index'
    loaded_index = faiss.read_index(index_filename)
    search_index=model.encode(Question)
    search_index=search_index.reshape(1,-1)
    _,I=loaded_index.search(search_index,k=5)
    result_context=""
    source=[]
    for _,ind in enumerate(I[0]):
        result_context+=docc[ind]
        if [metadata[ind]['source']] not in  source:
            source.append([metadata[ind]['source']])
    llm=OpenAI(temperature=0.7,)
    prompt_template = """Answer in very detail and Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}
    Answer:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    query_llm=LLMChain(llm=llm,prompt=prompt)
    response=query_llm.run({"context":result_context,"question":Question})
    return response, source

url_inputs = [gr.Textbox(lines=2, label=f"URL {i+1}") for i in range(2)]
iface = gr.Interface(fn=semantic_search, inputs=["text"]+url_inputs, outputs=["text", "list"])
iface.launch()
