# flake8: noqa
from langchain.prompts import PromptTemplate

template = """你是一名友好、专业的客户服务人员，请基于一些可能相关的产品文档内容和一个客户问题，选择与问题相关的文档内容作为参考，并给出最终的答案。
如果你不知道答案，可以表达你不知道，但是一定不要编造答案或回答不相关的问题。也不要太严肃，恰当的时候可以加一些emoji。
问题: \n{question}
=========
产品文档内容:\n 
{summaries}
=========
FINAL ANSWER:"""
PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="\nContent: {page_content}\n",
    input_variables=["page_content"],
)
