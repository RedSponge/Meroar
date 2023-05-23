from langchain import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

import constants
import guidelines

OPENAI_API_KEY = "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"

INPUT_VARIABLES = ["guidelines"]
# TEMPLATE = """
# This is a conversation over the phone between two participants.
# {conversation}
#
# You know the following things:
# Jason regularly exerts this kind of behaviour
#
# Explain the role of each participant in the conversation, and determine whether this relationship is unhealthy
# """

TEMPLATE = """
There are two people in a relationship. They just got off a phone call. 

Their phone call is problematic for the following reasons:
Mark is dismissive and unsupportive of Emma's ideas and does not seem to be listening to her. 
He is also belittling her efforts to make plans and is not showing respect for her choices. 
This conversation shows a lack of consideration for Emma's feelings and a disregard for her opinion.

Use the following guidelines when responding to the user. The guidelines are sorted by importance, with the most important on top.
{guidelines}
 
You're talking to Emma right after she got off the phone. 
Ask her how she's feeling and invite her to talk about it.
"""

prompt = PromptTemplate(template=TEMPLATE, input_variables=INPUT_VARIABLES)

memory = ConversationBufferMemory(memory_key="chat_history")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

agent = initialize_agent([], llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
agent.run(input=prompt.format(guidelines=guidelines.GUIDELINES))
responses = [
    ""
]
while True:
    agent.run(input=f'Human: {input("Enter your response: ")}')
# print(llm(prompt.format(conversation=constants.DUMMY_CONVERSATION, guidelines=guidelines.GUIDELINES)))
