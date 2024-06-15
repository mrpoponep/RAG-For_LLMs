import streamlit as st
from pymilvus import connections, Collection, utility
from pymilvus import utility
import google.generativeai as genai
from pymilvus import MilvusClient
from helper_func import create_prompt, process_data


connections.connect(uri=st.secrets.uri,token=st.secrets.token)
milvus_client = MilvusClient(uri=st.secrets.uri,token=st.secrets.token)
collection_name = "my_rag_collection2"

# Streamlit app
st.title("Insurance Q&A")

st.write("Ask a question and get an answer:")

embedding_model = 'models/text-embedding-004'
genai.configure(api_key=st.secrets.API_KEY)
def embed_fn(title, text):
  return genai.embed_content(model=embedding_model,
                             content=text,
                             task_type="retrieval_document",
                             title=title)["embedding"]

user_question = st.text_input("Your Question:")


if st.button("Get Answer"):
    search_res = milvus_client.search(
    collection_name=collection_name,
    data=[
        embed_fn(user_question,user_question)
    ],  # Use the `emb_text` function to convert the question to an embedding vector
    limit=7,  # Return top 3 results
    search_params={"metric_type": "COSINE",  "params": {"level": 2}}, # Inner product distance
    output_fields=["text"],  # Return the text field
)

    retrieved_lines_with_distances = [
        (res["entity"]["text"], res["distance"]) for res in search_res[0]]
    querry_data= process_data(retrieved_lines_with_distances)

    LLM_model = genai.GenerativeModel('gemini-pro')
    prompt=create_prompt(querry_data,user_question)
    response = LLM_model.generate_content(prompt)
    response =response.text.replace("JSON", "").replace("```","")
    st.success(f"Answer: {response}")
