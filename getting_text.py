from webbrowser import get
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
I want you to perform a data annotation task. In your output, I want you to return
either yes or no, depending on whether you think the following conversation is alarming.
A conversation is alarming if your perceive it alludes to an unhealthy relationship between the participants with Emma as the victim.
I want you to respond with yes or no in the first line and explain your assesment in the second line. The word "Summary:" and a summary of the conversation in the third line.

{conversation}
"""

# """
# You are about to recevie a conversation between two people. Emma and Mark, they are in a relationship.
# After reading the conversation, if you find the conversation toxic or problematic in any way, write description of the talk of what they talked about, only if the conversation is bad but do.
# if you do not find this conversation problematic, you need to respond only with the word 'OK'

# {conversation}
# """
# """
# If you find this conversation as problematic or toxic, you are not allowed to give any advice.
# you are only allowed to give a summary of this conversation without expressing any advise/opinion/help.
# explain what happen in their conversation and way it is problematic using details of the situation from indifferent point of view.
# otherwise, return a just the word "OK", without any explanation.
# """

prompt = PromptTemplate(template=TEMPLATE, input_variables=INPUT_VARIABLES)
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

def get_insight_from_conversation(conversation: str):
    return llm(prompt.format(conversation=conversation))

if __name__ == "__main__":
    print(get_insight_from_conversation(constants.BAD_CONVERSATION_2))