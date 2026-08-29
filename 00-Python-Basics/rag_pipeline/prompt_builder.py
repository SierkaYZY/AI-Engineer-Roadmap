
# 将返回的向量匹配度高的内容重新整理并输出
def build_context(results):
    """
    将返回的向量匹配度高的内容重新整理并输出
    Args:
        results(dict):
            存放多个高匹配文档内容和信息的字典
    Returns:
        str:
            整理完成后的完整资料信息
    """
    documents = results["documents"][0]
    formatted_documents = []
    for index,item in enumerate(documents,start=1):
        format_document = (f"[资料{index}]\n{item}")
        formatted_documents.append(format_document)
    context = "\n\n".join(formatted_documents)
    return context

# 构建提示词prompt
def build_prompt(query,context):
    """
    根据用户问题和参考资料构造完整提示词。
    Args:
        query(str):
            用户问题
        context(str):
            检索并整理后的参考资料
    Returns:
        str:
            完整的提示词
    """
    prompt = f"""你是一个知识库问答助手。
请根据提供的参考资料回答问题。
如果参考资料不足，请说明资料不足，不要编造答案。

参考资料：
{context}

用户问题:
{query}

回答:
    """
    return prompt

# 测试
if __name__ == "__main__":
    results = {
    "documents": [
        [
            "Apple is a fruit.",
            "Bananas are yellow."
            ]
        ]
    }
    query = "What color are bananas?"

    context = build_context(results)

    prompt = build_prompt(query, context)

    print(prompt)

