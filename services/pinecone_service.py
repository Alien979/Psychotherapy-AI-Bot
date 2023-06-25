import pinecone
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from pinecone import Vector

pinecone.init(api_key='#ENTER YOUR OPEN PINECONE API KEY HERE', environment='ENTER PINECONE ENVIRONMENT HERE')
index_name = "mental-health-support"

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/bert-base-nli-mean-tokens")
model = AutoModel.from_pretrained("sentence-transformers/bert-base-nli-mean-tokens")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)  # We take the mean of the word embeddings to get sentence embedding
    return embeddings.detach().numpy()  # Convert the PyTorch tensor to a numpy array

def check_index():
    index_name = "chatbot-index"
    dimension = 768  # Adjust based on your embeddings' dimension
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, metric="cosine", shards=1, dimension=dimension)

# Function to get index instance
def get_index():
    return pinecone.Index(index_name=index_name)


def update_vectors(user_id, message, openai_response, cohere_response):
    index = get_index()

    # Convert the messages to embeddings
    user_embedding = get_embedding(message)
    openai_embedding = get_embedding(openai_response)
    cohere_embedding = get_embedding(cohere_response)

    # Convert the numpy array embeddings to lists
    user_embedding_list = user_embedding[0].tolist()
    openai_embedding_list = openai_embedding[0].tolist()
    cohere_embedding_list = cohere_embedding[0].tolist()

    # Create vectors with the embeddings
    user_vector = Vector(id=f'{user_id}-user', values=user_embedding_list)
    openai_vector = Vector(id=f'{user_id}-openai', values=openai_embedding_list)
    cohere_vector = Vector(id=f'{user_id}-cohere', values=cohere_embedding_list)

    # Perform the upsert with all vectors in a batch
    try:
        _ = index.upsert(vectors=[user_vector, openai_vector, cohere_vector])
    except Exception as e:
        print(f"Error: {e} occurred during upsert")
