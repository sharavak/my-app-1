from my_first_crew_app.crew import MyFirstCrewApp
from dotenv import load_dotenv
import os

load_dotenv()  # 🔥 This loads .env file
def run():
    result = MyFirstCrewApp().crew().kickoff(
        inputs={"topic": "What is the current gold rate in chennai?"}
    )
    print(result)