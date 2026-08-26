# 调用模块内函数
# 调用文档读取函数
from file_io.document_loader import load_txt
# 调用文档信息创建函数
from data_structures.document_analyzer import build_document

def process_txt(path,filename):
    """
    阅读文档并创建文档信息
    Args:
        path(str):
            文件路径
        filename(str):
            文件名
    Returns:
        dict:
            文档信息
    """
    text = load_txt(path)
    if text is None:
        return None
    document_info = build_document(filename,text)
    return document_info

# 测试检验函数
if __name__=="__main__":
    path="file_io/test.txt"
    filename= "test.txt"
    document_info=process_txt(path,filename)
    if document_info is None:
        print(f"无法读取文件:{path}")
    else:
        print(document_info["content"])
        print(document_info["metadata"])
        print(document_info["metadata"]["filename"])
        print(document_info["metadata"]["word_count"])