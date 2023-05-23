from langchain import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

import constants

OPENAI_API_KEY = "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"

INPUT_VARIABLES = ["conversation"]
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
There are two people in a relationship.
This is a conversation between them:

{conversation}

If the conversation doesn't contain any unhealthy behaviour, the word "OK" will appear. 

Otherwise, if the conversation has problematic or abusive connotations, the word "BAD" and the following information will appear:
1. An indifferent summary of the conversation explaining what happened, devoid of any advise, opinion or help.
2. An explanation why this conversation is not good, using details that are based on the conversation context

you are not allowed to give any advice

"""
# """
# If you find this conversation as problematic or toxic, you are not allowed to give any advice.
# you are only allowed to give a summary of this conversation without expressing any advise/opinion/help.
# explain what happen in their conversation and way it is problematic using details of the situation from indifferent point of view.
# otherwise, return a just the word "OK", without any explanation.
# """

prompt = PromptTemplate(template=TEMPLATE, input_variables=INPUT_VARIABLES)

memory = ConversationBufferMemory(memory_key="chat_history")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

agent = initialize_agent([], llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
agent.run(input=prompt.format(conversation=constants.BAD_CONVERSATION))
responses = [
    ""
]
while True:
    agent.run(input=f'Human: {input("Enter your response: ")}')
# print(llm(prompt.format(conversation=constants.DUMMY_CONVERSATION, guidelines=guidelines.GUIDELINES)))
