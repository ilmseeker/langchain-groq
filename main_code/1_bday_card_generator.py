from langchain_core.prompts import PromptTemplate
from prompts.bday_card_prompt import BDAY_CARD_PROMPT
from llm_object import llm

def create_bday_card(name: str):
    prompt = PromptTemplate(template=BDAY_CARD_PROMPT, input_variables=["name"])
    prompt = BDAY_CARD_PROMPT.format(name=name)
    return(print(llm.invoke(prompt).content))


create_bday_card("Haider")