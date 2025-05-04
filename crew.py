import json
from crewai import Crew,Process
from agents import observability_agent
from tasks import observability_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[observability_agent],
    tasks=[observability_task],
    verbose=True,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    process=Process.sequential,  # Optional: Sequential task execution is default
)

## start the task execution process with enhanced feedback
crew_output=crew.kickoff(inputs={'topic':'Get disk occupation'})

# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
    print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
    print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")
    
# print(result.output)
