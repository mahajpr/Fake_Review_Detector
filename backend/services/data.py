
import faiss
import os
import numpy as np
from groq import Groq
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("all-MiniLM-L6-v2")


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_chunks(text , source , chunk_size =200):
    chunks=[]
    for i in range(0 , len(text),chunk_size):
        chunks.append({
            "text":text[i:i+chunk_size],
            "source":source
        })
    return chunks

def load_folders(folder_path="reviews"):
    all_chunks=[]
    for file in  os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                text = f.read().strip()
                chunks = load_chunks(text, file)
                all_chunks.extend(chunks)
    return all_chunks

def embedding(chunk):
    embedded_value = embed_model.encode(chunk)
    if len(embedded_value.shape)==1:
        embedded_value = embedded_value.reshape(1,-1)
    return embedded_value

def create_index(embedded_data):
    dim = embedded_data.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embedded_data))
    return index

def search(chunks,query,index,top_k=10):
    query_embed = embed_model.encode(query)
    if len(query_embed.shape)==1:
        query_embed = query_embed.reshape(1,-1)
    distance, indices = index.search(np.array(query_embed),top_k)
    result = []
    for i in indices[0]:
        result.append(chunks[i])
    return result

def response(query,context):
    context_data = ""
    for data in context:
        context_data = context_data + data['text'] + "\n"
        context_data = context_data + data["source"] + "\n\n"
    prompt = f"""
    Answer only from the following context
    context: {context_data}
    input: {query}
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
    )
    return completion.choices[0].message.content


def get_rag_context(review_text):
    chunks = load_folders()
    texts = [c["text"] for c in chunks]
    embedding= embed_model.encode(texts, convert_to_numpy=True)
    index = create_index(embedding)
    context = search(chunks, review_text, index)
    return context
