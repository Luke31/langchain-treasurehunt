from actor.agents import main_agent
from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def run():
    # api_docs = apidocs.get_docs()
    # result = hunter_agent.hunt_for_treasure(api_docs)
    result = main_agent.run_main_agent()
    print(result)


if __name__ == "__main__":
    run()