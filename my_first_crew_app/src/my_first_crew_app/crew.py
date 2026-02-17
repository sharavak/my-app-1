# CrewBase:
# Reads YAML files in the project folder
# Stores them in:
# self.agents_config
# self.tasks_config
# Processes @agent, @task, and @crew decorators
# Builds final Crew object

from crewai import Crew, Process,Agent,Task
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool


@CrewBase
class MyFirstCrewApp():

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    # @agent
    # def writer(self)-> Agent:
    #     return Agent(
    #      config= self.agents_config["writer"],
    #      verbose=True
    #     )

    @task
    def researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    # @task
    # def writer_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['writer_task'], # type: ignore[index]
    #     )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )