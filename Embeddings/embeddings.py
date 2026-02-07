from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

documents = [
    "My name is Abdullah",
    "My name is khan",
    "My name is izhan"
]

query = "abc"

embedding_query = embeddings.embed_query(query)
embedding_docs = embeddings.embed_documents(documents)

scores = cosine_similarity([embedding_query], embedding_docs)[0]
index , score = sorted(list(enumerate(scores)),key=lambda x: x[1], reverse=True)[0]
print(documents[index])
