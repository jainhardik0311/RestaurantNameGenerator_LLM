from secretkey import openapi_key
import os
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):

    # Chain 1: Restaurant Name
    prompt_restaurant_name = PromptTemplate(
        input_variables= ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Only one name please"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_restaurant_name, output_key = "restaurant_name")

    # Chain 2: Restaurant Description
    prompt_restaurant_desc = PromptTemplate(
        input_variables= ['restaurant_name'],
        template = "Provide me a 50 words catchy description for this {restaurant_name}"
    )

    desc_chain = LLMChain(llm=llm, prompt=prompt_restaurant_desc, output_key = "restaurant_desc")

    # Chain 3: Restaurant Item
    prompt_restaurant_items = PromptTemplate(
        input_variables= ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated value."
    )

    item_chain = LLMChain(llm=llm, prompt=prompt_restaurant_items, output_key = "menu_items")

    chain = SequentialChain(
        chains = [name_chain, desc_chain, item_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name','restaurant_desc','menu_items']
        )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))