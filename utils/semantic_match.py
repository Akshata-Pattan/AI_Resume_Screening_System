from sentence_transformers import SentenceTransformer, util

# Model is NOT loaded during app startup
model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def semantic_similarity(resume_text, job_description):
    model = get_model()

    embedding1 = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    embedding2 = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        embedding1,
        embedding2
    )

    return float(similarity[0][0] * 100)