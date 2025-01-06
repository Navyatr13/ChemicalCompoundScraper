from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_search(query, documents, top_k=5):
    """
    Perform semantic search for a query across a list of documents.
    """
    query_embedding = model.encode(query, convert_to_tensor=True)
    document_embeddings = model.encode(documents, convert_to_tensor=True)

    cosine_scores = util.cos_sim(query_embedding, document_embeddings)
    top_results = cosine_scores.topk(k=top_k)

    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        results.append((documents[idx], score.item()))
    return results
