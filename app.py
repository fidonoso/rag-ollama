import streamlit as st
import os
from utils import *
from langchain_huggingface import HuggingFaceEmbeddings #utiliza modelos de HuggingFace para generar embeddings de texto.
from langchain.chains.question_answering import load_qa_chain #Importa una función para cargar cadenas de preguntas y respuestas.

from langchain_community.llms import Ollama # para usar los modelos locales de ollama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

from langchain.prompts import PromptTemplate # clase para manejar plantillas de prompts.
from langchain.chains import RetrievalQA #  Importa la cadena de preguntas y respuestas basada en la recuperación de documentos.

st.set_page_config('Chat Docs')
st.header("Pregunta a tus PDF's")

with st.sidebar:
    # option = st.selectbox("Ubicación del modelo",("Local con Ollama", "Remoto"))
    
    archivos = load_name_files(FILE_LIST)
    files_uploaded = st.file_uploader(
        "Carga tus archivos",
        type="pdf",
        accept_multiple_files=True
        )
    
    if st.button('Procesar'):
        for pdf in files_uploaded:
            if pdf is not None and pdf.name not in archivos:
                archivos.append(pdf.name)
                text_to_chromadb(pdf)

        archivos = save_name_files(FILE_LIST, archivos)

    if len(archivos) > 0:
        st.write("Archivos cargados:")
        lista_documentos = st.empty()
        with lista_documentos.container():
            for arch in archivos:
                st.write(arch)
            if st.button('Borrar documentos'):
                archivos = []
                clean_files(FILE_LIST)
                lista_documentos.empty()

if archivos:
    user_question = st.text_input("Pregunta:")
    if user_question:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            )
        
        vstore = Chroma(client=chroma_client,
                        collection_name=INDEX_NAME,
                        embedding_function=embeddings)
        
        custom_prompt_template = """Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        Question: {question}

        Only return the helpful answer below and nothing else but in spanish.
        Helpful answer:
        """
        prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

        docs = vstore.as_retriever(search_kwargs={'k': 4})
        llm = Ollama(model="llama3.1:latest")

        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=docs,
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )

        respuesta = qa.invoke({"query": user_question})
        metadata = []
        for _ in respuesta['source_documents']:
            metadata.append(('page: '+str(_.metadata['page']),  os.path.basename(_.metadata['source'])))
        resp2=respuesta["result"]
        unicos = set()
        for elemento in metadata:
            unicos.add(f"{elemento[0]} - {elemento[1]}\n")

        resMetdata="\n".join(sorted(unicos))    
        st.write(resp2)
        st.write(resMetdata)
        
        
        
        # streamlit run app.py