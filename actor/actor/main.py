from langchain.callbacks import StreamlitCallbackHandler

from actor.agents import hunter_agent, main_agent
from dotenv import load_dotenv
import os
import openai

from actor.third_parties import apidocs

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def run(st_callback: StreamlitCallbackHandler, model="gpt-4"):
    api_docs = apidocs.get_docs()
    result = hunter_agent.hunt_for_treasure(api_docs, st_callback, model)
    # result = main_agent.run_main_agent()
    # print(result)
    return result


if __name__ == "__main__":
    run()