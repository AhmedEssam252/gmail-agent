
from composio_crewai import ComposioToolSet, Action
from crewai import Agent, Task, Crew
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1")

tool_set = ComposioToolSet()
tools = tool_set.get_tools(actions=[Action.GMAIL_SEND_EMAIL])

# Define agent
crewai_agent = Agent(
    role="Gmail Agent",
    goal="""You take action on Gmail using Gmail APIs""",
    backstory=(
        "You are AI agent that is responsible for taking actions on Gmail "
        "on users behalf. You need to take action on Gmail using Gmail APIs"
    ),
    verbose=True,
    tools=tools,
    llm=llm,
)

sender = "ahmed.essam.252252@gmail.com"
receiver = "microahmed252@outlook.com"


task = Task(
    description=f"Send an email from {sender} to {receiver} explaining what Crew-AI is and provide a real-life example of how it can enhance productivity.",
    agent=crewai_agent,
    expected_output="if the mail sent successfully"
)
my_crew = Crew(agents=[crewai_agent], tasks=[task])

result = my_crew.kickoff()
print(result)
