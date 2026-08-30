# 函数调用
from rag_pipeline.query_database import query_document
from rag_pipeline.prompt_builder import build_context, build_prompt
from llm.llm_client import generate_answer
from retrieval.result_filter import filter_results_by_distance

#  根据知识库检索结果生成最终回答
def rag_answer(
        query, 
        model_name, 
        top_k=2,
        max_distance = 0.95,
        debug= False
    ):
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

    raw_results = query_document(query,model_name,top_k)

    results = filter_results_by_distance(
    raw_results,
    max_distance
    )

    if not results["documents"][0]:
        return "没有找到足够相关的参考资料，无法回答该问题。"

    context = build_context(results)
    
    prompt = build_prompt(query,context)

    if debug:
        print("=== Raw Retrieval Results ===")

        raw_ids = raw_results["ids"][0]
        raw_distances = raw_results["distances"][0]

        for i in range(len(raw_ids)):
            print(f"{raw_ids[i]} | distance: {raw_distances[i]}")

        print("=== Filtered Retrieval Results ===")

        ids = results["ids"][0]
        distances = results["distances"][0]

        for i in range(len(ids)):
            print(f"{ids[i]} | distance: {distances[i]}")

    answer = generate_answer(prompt)
    
    return answer

# 测试
if __name__ == "__main__":
    query = "What is the capital of France?"
    model_name = "BAAI/bge-small-zh-v1.5"
    answer = rag_answer(query,model_name,debug=True)
    print("=== Answer ===")
    print(answer)