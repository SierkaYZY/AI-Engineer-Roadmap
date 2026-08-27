from sentence_transformers import SentenceTransformer
from embedding.similarity import cosine_similarity
from file_io.document_processor import process_txt


#在chunk中引入嵌入向量
def embed_chunks(chunks,model):
    """
    在块中引入嵌入向量
    Args:
        chunks(list[dict]):
            文本的分块
        model:
            已加载的 SentenceTransformer 模型对象
    Returns:
        list[dict]:
            引入嵌入向量后的块
    """ 
    texts = []
    for chunk in chunks: 
        texts.append(chunk["content"])

    embeddings = model.encode(texts,normalize_embeddings=True)

    embedded_chunks = []
    for chunk,embedding in zip(chunks,embeddings):
        embedded_chunk = {
             "content":chunk["content"],
             "metadata":chunk["metadata"].copy(),
             "embedding":embedding.tolist()
        }
        embedded_chunks.append(embedded_chunk)
    return embedded_chunks

# 测试    
if __name__ == "__main__":
        path = "file_io/test.txt"
        chunks = process_txt(path,6,2)
        model_name = "BAAI/bge-small-zh-v1.5"
        model = SentenceTransformer(model_name)
        embedded_chunks = embed_chunks(chunks,model)
        print(len(embedded_chunks))
        print(embedded_chunks[0]["content"])
        print(embedded_chunks[0]["metadata"])
        print(len(embedded_chunks[0]["embedding"]))
        print(embedded_chunks[0]["embedding"][:5])