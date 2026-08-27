
# 文本切片
def split_text(text,chunk_size,chunk_overlap=0):
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
    if not 0 <= chunk_overlap < chunk_size:
        raise ValueError("chunk_overlap 必须满足 0 <= chunk_overlap < chunk_size")
    step = chunk_size - chunk_overlap
    chunks=[]
    for i in range(0,len(text),step):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
        if i+chunk_size >= len(text) :
            break
    return chunks

# 文本字典切片
def split_document(document,chunk_size,chunk_overlap=0):
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
    text_chunks= split_text(text,chunk_size,chunk_overlap)
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
    print(split_text("abcdefghij", 4))
    print(split_text("abcdefghij", 4, 1))
    document = {
    "content": "abcdefghij",
    "metadata": {
        "filename": "test.txt"
        }
    }
    print(split_document(document, 4, 1))
    print(split_text("abcdefghij", 4, 4))
    