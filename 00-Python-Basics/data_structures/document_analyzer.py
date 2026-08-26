# 调用text_tool.py的函数
from function.text_tool import count_chars, count_words

# 任务一:把文本转换成行列表
def get_valid_lines(text):
    """
    将文本转换成行列表,并删除空行
    Args:
        text(str):
            输入文本
    Returuns:
        list:
            文本行列式
    """
    lines=text.split("\n")
    valid_lines=[] 
    for line in lines:
        if line.strip()!= "":
            valid_lines.append(line)
    return valid_lines 
# 不要忘了return返回值,否则返回none,会导致后续的代码报错

# 任务二:创建文档信息字典
def build_document_info(filename, text):
    """
    创建文档信息字典
    Args:
        filename(str):
            文档名
        text(str):
            文档内容
    Returns:
        dict:
            文档信息字典
    """
    valid_lines = get_valid_lines(text)
    return{
        "filename":filename,
        "line_count":len(valid_lines),
        "char_count":count_chars(text),
        "word_count":count_words(text)
    }

# 任务三:处理多个文档
def analyze_doucuments(documents):
    """
    处理多个文档,并返回文档信息字典列表
    Args:
        documents(list):
            文档信息列表
    Returns:
        list:
            文档字典信息列表
    """
    doucument_info_list=[]
    for document in documents:
            document_info=build_document_info(document["filename"],document["text"])
            doucument_info_list.append(document_info)
    return doucument_info_list
        
# 测试
if __name__=="__main__":
    #测试get_valid_lines函数
    text="Hello world!\n\nthis is a test.\n\n\nPython is great!"
    valid_lines=get_valid_lines(text)
    print("有效行:", valid_lines)  # 输出: ['Hello world!', 'this is a test.', 'Python is great!']
    # 测试build_document_info函数
    filename="test.txt"
    document_info=build_document_info(filename, text)
    print("单文档信息:", document_info)  # 输出: {'filename': 'test.txt', 'line_count': 3, 'char_count': 44, 'word_count': 9}
    # 测试analyze_doucuments函数
    documents=[
        {"filename": "doc1.txt", "text": "Hello world!\n\nthis is a test.\n\n\nPython is great!"},
        {"filename": "doc2.txt", "text": "Another document.\nWith some text.\n\nAnd more text."}
    ]
    document_info_list=analyze_doucuments(documents)
    print("多文档信息:", document_info_list)  # 输出: [{'filename': 'doc1.txt', 'line_count': 3, 'char_count': 44, 'word_count': 9}, {'filename': 'doc2.txt', 'line_count': 3, 'char_count': 49, 'word_count': 10}]
    