# 读取TXT文件内容
def load_txt(path):
    """
    读取TXT文件内容
    Args:
        path(str):
            文件路径
    Returns:
        str:
            文件中的文件内容
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        return None

# 测试检验函数
if __name__=="__main__":
    paths=["file_io/test.txt", "file_io/not_exist.txt"]
    for path in paths:
        print(f"正在读取文件:{path}")
        text = load_txt(path)
        if text is None:
            print(f"无法读取文件:{path}")
        else:
            print(f"文件内容:\n{text}")