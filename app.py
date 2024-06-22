import streamlit as st
from pymilvus import connections
import google.generativeai as genai
from pymilvus import MilvusClient
from helper_func import create_prompt, process_data

collection_name = "my_rag_collection2"
connections.connect(uri=st.secrets.uri,token=st.secrets.token)
milvus_client = MilvusClient(uri=st.secrets.uri,token=st.secrets.token)

embedding_model = 'models/text-embedding-004'
genai.configure(api_key=st.secrets.API_KEY)
def embed_fn(title, text):
  return genai.embed_content(model=embedding_model,
                             content=text,
                             task_type="retrieval_document",
                             title=title)["embedding"]

def embed_fn(title, text):
  return genai.embed_content(model=embedding_model,
                             content=text,
                             task_type="retrieval_document",
                             title=title)["embedding"]

with st.sidebar:
    st.title("💬 Insurance Assistant")
    st.write("I can answer popular insurance questions based on expert responses.")
    st.page_link("https://github.com/mrpoponep/RAG-For_LLMs/blob/main/Misc/Example_data.jsonl",label="Example questions")

LLM_model = genai.GenerativeModel('gemini-pro')

if "chat" not in st.session_state:
    st.session_state.chat = genai.GenerativeModel('gemini-pro').start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.session_state.chat = genai.GenerativeModel('gemini-pro').start_chat(history=[])
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Processing..."):
        try:
            search_res = milvus_client.search(
                collection_name=collection_name,
                data=[
                    embed_fn(prompt,prompt)
                ],  # Use the `emb_text` function to convert the question to an embedding vector
                limit=7,  # Return top 3 results
                search_params={"metric_type": "COSINE",  "params": {"level": 2}}, # Inner product distance
                output_fields=["text"],  )

            retrieved_lines_with_distances = [
                    (res["entity"]["text"], res["distance"]) for res in search_res[0]]
            querry_data= process_data(retrieved_lines_with_distances)
            
            prompt=create_prompt(querry_data,prompt)
            
            response = st.session_state.chat.send_message(prompt)
            response =response.text.replace("JSON", "").replace("```","")

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
        except:
            st.error("Error occurred. Please try again later.")