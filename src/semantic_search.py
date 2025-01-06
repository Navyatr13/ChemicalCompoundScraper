from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
def semantic_search(query, documents, top_k=5):
    # Ensure documents are not empty
    if not documents:
        print("No documents available for semantic search.")
        return []

    # Initialize the model
    model = SentenceTransformer("all-mpnet-base-v2")

    # Compute embeddings
    query_embedding = model.encode(query, convert_to_tensor=True)
    document_embeddings = model.encode(documents, convert_to_tensor=True)
    print(document_embeddings)

    # Compute cosine similarity
    cosine_scores = util.cos_sim(query_embedding, document_embeddings)
    print(cosine_scores)

    # Adjust top_k if it exceeds the number of documents
    top_k = min(top_k, len(documents))

    # Get the top results
    top_results = cosine_scores.topk(k=top_k)
    results = []
    for idx in top_results.indices[0]:  # Access the first row of indices
        idx_int = idx.item()  # Convert tensor element to a Python integer
        print(idx_int)
        print(idx_int, documents[idx_int])
        results.append((documents[idx_int], float(cosine_scores[0, idx_int])))

    return results

if __name__ == "__main__":
    query = "Anti-inflammatory effects of Aspirin"
    documents = [
        "Aspirin inhibits COX1 and COX2.",
        "Ibuprofen reduces inflammation via prostaglandins.",
        "Paracetamol affects pain relief mechanisms."
    ]
    res = semantic_search(query, documents, top_k=2)
    print(res)