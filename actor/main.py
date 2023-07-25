from agents import hunter_agent
from third_parties import apidocs
from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def run():
    api_docs = apidocs.get_docs()
    result = hunter_agent.hunt_for_treasure(api_docs)
    print(result)


if __name__ == "__main__":
    run()