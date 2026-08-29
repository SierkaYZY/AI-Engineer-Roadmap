# 函数调用
from rag_pipeline.query_database import query_document
from rag_pipeline.prompt_builder import build_context, build_prompt
from llm.llm_client import generate_answer

#  根据知识库检索结果生成最终回答
def rag_answer(query, model_name, top_k=2,debug= False):
    """
    根据知识库检索结果生成最终回答。

    Args:
        query (str):
            用户问题。
        model_name (str):
            Embedding 模型名称。
        top_k (int):
            检索返回的相关文本数量。

    Returns:
        str:
            大语言模型生成的最终回答。
    """

    results = query_document(query,model_name,top_k)

    context = build_context(results)
    
    prompt = build_prompt(query,context)

    if debug:
        print("=== Context ===")
        print(context)

        print("=== Prompt ===")
        print(prompt)

    answer = generate_answer(prompt)
    
    return answer

# 测试
if __name__ == "__main__":
    query = "What is the capital of France?"
    model_name = "BAAI/bge-small-zh-v1.5"
    answer = rag_answer(query,model_name,debug=True)
    print("=== Answer ===")
    print(answer)