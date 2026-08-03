from sentence_transformers import SentenceTransformer, util

# Load AI Model (loads only once)
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(resume_text, job_description):

    embedding1 = model.encode(resume_text, convert_to_tensor=True)
    embedding2 = model.encode(job_description, convert_to_tensor=True)

    similarity = util.cos_sim(embedding1, embedding2)

    return float(similarity[0][0] * 100)