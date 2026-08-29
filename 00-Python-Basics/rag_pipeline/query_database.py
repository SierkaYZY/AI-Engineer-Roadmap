# 函数调用
import chromadb
from sentence_transformers import SentenceTransformer
from vector_store.chroma_store import search_chunks

# 连接已有数据库输出与用户输入文本相关性高的结果
def query_document(query,model_name,top_k=2):
    """
    连接已有数据库检索与用户文本相似度高的结果并输出结果
    Args:
        query(str):
            用户输入文本
        model_name(str):
            所调用的切片转换向量的模型的名字
        top_k(int):
            取几个相似度高的结果
    Returns:
        dict:
            输出的相似度较高的结果
    """
    client = chromadb.PersistentClient(path = "./chroma_db")
    collection = client.get_collection(name="knowledge_chunks")
    model = SentenceTransformer(model_name)

    results = search_chunks(collection,query,model,top_k)
    return results

# 测试
if __name__ == "__main__":
    query = input("请输入问题:")
    top_k = 2
    model_name = "BAAI/bge-small-zh-v1.5"
    results = query_document(query,model_name,top_k)
    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    for i in range(len(ids)):
        print(f"\n第{i + 1}条结果")
        print(f"ID:{ids[i]}")
        print(f"距离：{distances[i]}")
        print(f"文本：{documents[i]}")
        print(f"元数据：{metadatas[i]}")
