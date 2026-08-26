# 调用函数


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

# 测试
if __name__=="__main__":
    text = "Artificial intelligence is changing software development."
    chunks = split_text(text,20)
    print(chunks)

