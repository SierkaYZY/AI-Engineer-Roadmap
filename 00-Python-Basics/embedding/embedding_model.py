from sentence_transformers import SentenceTransformer
from embedding.similarity import cosine_similarity
# 第一版测试
MODEL_NAME = "BAAI/bge-small-zh-v1.5"


if __name__ == "__main__":
    model = SentenceTransformer(MODEL_NAME)

    texts = [
    "人工智能正在改变软件开发",
    "AI正在改变程序开发方式",
    "今天天气很好"
    ]

    embeddings = model.encode(texts,normalize_embeddings=True)
    similarity_score = cosine_similarity(embeddings[0],embeddings[1])
    unrelated_score = cosine_similarity(embeddings[0],embeddings[2])

    print(texts[0], "<->", texts[1])
    print("相似度：", similarity_score)

    print(texts[0], "<->", texts[2])
    print("相似度：", unrelated_score)