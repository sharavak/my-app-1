from crewai import Crew,Agent,Process,Task
from crewai.project import agent,task,crew,CrewBase
from crewai_tools import SerperDevTool
@CrewBase
class MyFirstCrewwApp():
    @agent
    def researcher(self)->Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )
    @agent
    def writer(self)->Agent:
        return Agent(
            config=self.agents_config["writer"],
            verbose=True
        )
    @task
    def reseacher_task(self)->Task:
     return Task(
        config=self.tasks_config['research_task'],
        # agent=researcher
    )
    @task
    def writer_task(self)->Task:
     return Task(
        config=self.tasks_config['writer_task'],
        # agent=writer
    )
    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
