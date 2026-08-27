# 调用函数
from data_structures.document_analyzer import build_document

# 文本切片
def split_text(text,chunk_size):
    """
    对文本按指定长度切片
    Args:
        text(str):
            文本内容
        chunk_size(int):
            切片的长度
    Returns:
        list:
            切片后的文本
    """
    chunks=[]
    for i in range(0,len(text),chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

# 文本字典切片
def split_document(document,chunk_size):
    """
    对读取文本后的字典按指定长度切片
    Args:
        documnet(dict):
            文档信息字典
        chunk_size(int):
            切片长度
    Returns:
        list:
            切片后的字典
    """
    text= document["content"]
    text_chunks= split_text(text,chunk_size)
    chunks = []
    for chunk_id,chunk_text in enumerate(text_chunks):
        chunk_metadata= document["metadata"].copy()
        chunk_metadata["chunk_id"]= chunk_id
        chunk= {
            "content":chunk_text,
            "metadata":chunk_metadata
        }
        chunks.append(chunk)
    return chunks

# 测试
if __name__=="__main__":
    document = {
    "content": "abcdefghij",
    "metadata": {
        "filename": "test.txt"
    }
}
    chunks = split_document(document, 4)
    print(chunks)
    print(document)
