from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os
from secretkey import openapi_key

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

tools = load_tools(["wikipedia","llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbrose = True
)

# response = agent.run("When was Elon Musk born? What is his age right now in 2023?")
# print(response)