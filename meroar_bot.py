from bisect import insort_right
from langchain import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

import constants
from getting_text import get_insight_from_conversation
import guidelines

OPENAI_API_KEY = "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"

problems = """Mark is dismissive and unsupportive of Emma's ideas and does not seem to be listening to her. 
He is also belittling her efforts to make plans and is not showing respect for her choices. 
This conversation shows a lack of consideration for Emma's feelings and a disregard for her opinion."""

INPUT_VARIABLES = ["guidelines", "problems"]

TEMPLATE = """
There are two people in a relationship. They just got off a phone call. 

This is the summary of their latest conversation:
{problems}

Use the following guidelines when responding to the user. The guidelines are sorted by importance, with the most important on top.
{guidelines}
 
You're talking to Emma right after she got off the phone. 
Ask her how she's feeling and invite her to talk about it.
"""

print("Guidelines:", guidelines.GUIDELINES)
prompt = PromptTemplate(template=TEMPLATE, input_variables=INPUT_VARIABLES)

memory = ConversationBufferMemory(memory_key="chat_history")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

conversation = constants.BAD_CONVERSATION_2
insight = get_insight_from_conversation(conversation).strip()
print(insight)
if insight.startswith("Yes"):
    problems = insight.split('Summary:')[1]

    agent = initialize_agent([], llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory)
    agent.run(input=prompt.format(guidelines=guidelines.GUIDELINES, problems=problems))
    while True:
        agent.run(input=f'Human: {input("Enter your response: ")}')
else:
    print("This conversation looks good!")
