from dotenv import load_dotenv
from my_first_creww_app.crew import MyFirstCrewwApp
import os
load_dotenv()
def run():
    result=MyFirstCrewwApp().crew().kickoff(
        inputs={"topic":"what is the current gold rate in chennai?"}
    )
    print(result)
    