from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

from actor.agents.rest_agent import run_rest_agent

model_main_agent = "gpt-3.5-turbo"
model_rest_agent = "gpt-3.5-turbo"


def run_main_agent() -> str:
    prefix = f"""
        You are on a 2D-grid and can see on the current and directly to adjacent cells.
        Goal of the game: You need to find and pick up the treasure. You also know the distance to the treasure.
        Goal of agent: Send commands to reach the goal. Rephrase the previous response in natural words before taking the next action.
        Determine each command based on the previous response for the current given situation while considering the past taken steps.
        Stop when you have reached the treasure.

        Rules of the game:
        - Cell descriptions: W=wall, G=ground, T=treasure
        - Available commands (choose freely): START UP DOWN LEFT RIGHT PICK_UP
        - You can only pick up the treasure if the current cell has the treasure on it and is not a ground.
        - Do NOT attempt to pick up the treasure if it's in an adjacent cell. Wait until you have reached it.
        - Do NOT walk towards adjacent cells with walls. Wall-cells are marked by the letter 'W'.
        - Do NOT start the game again until you have found the treasure.
        - The previous observation already contains the current adjacent cells.
        """
    agent = initialize_agent(
        tools=[
            Tool(
                name="RestAgent",
                func=run_rest_agent,
                description="""useful when you need to call the api to send the command and return the content of the response
                DO NOT SEND THE ACTUAL REQUEST TO THIS TOOL. JUST SEND THE COMMAND.""",
            ),
        ],
        llm=ChatOpenAI(temperature=0, model=model_main_agent),
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )
    return agent.run(prefix + "\nStart the game and find the treasure")