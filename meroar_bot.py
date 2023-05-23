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
There are two people in a relationship. Emily and Mark

This is your known state:
Each entry will be formatted this way:
date: details
20/05/23: Mark was disrespectful
21/05/23: Mark was disrespectful
22/05/23: Mark was controlling
22/05/23: Emily tried to compromise

Use the following guidelines when responding to the user. The guidelines are sorted by importance, with the most important on top.
{guidelines}
 
You're talking to Emily. Ask her how she's feeling and invite her to talk about it.
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
