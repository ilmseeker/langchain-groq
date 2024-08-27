from langchain_core.prompts import PromptTemplate
from prompts.text_for_summary import TEXT_TO_SUMMARIZE
from templates.summary_generation_template import SUMMARY_GENERATION_TEMPLATE
from langchain_core.output_parsers import StrOutputParser
from llm_object import llm


#### Summary Generation #####

def generate_summary(content: str):
    prompt = PromptTemplate(template=SUMMARY_GENERATION_TEMPLATE, 
                            input_variables=["content"])
    output_parser = StrOutputParser() # parse the text
    chain = prompt | llm | output_parser
    return(print(chain.invoke({"content": content})))


text_context = TEXT_TO_SUMMARIZE

generate_summary(text_context)