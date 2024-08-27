from langchain_core.prompts import ChatPromptTemplate
from templates.basic_qna_with_context import BASIC_QNA_WITH_CONTEXT_TEMPLATE
from llm_object import llm
import itertools


#### Basic QNA with Context History #####

qna_with_context_prompt = ChatPromptTemplate.from_template(template=BASIC_QNA_WITH_CONTEXT_TEMPLATE)
qna_with_context_chain = qna_with_context_prompt | llm

def handle_conversation(chain):
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chain.invoke({"context": context, "question": user_input})
        print(f"""'Bot: '{response.content}\n'tokens data':\n{dict(itertools.islice(response.response_metadata['token_usage'].items(), 3))}""")
        context += f"\nUser: {user_input}\nAI: {response.content}"

if __name__ == "__main__":
    handle_conversation(qna_with_context_chain)