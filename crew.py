from crewai import Crew,Process
from agents import observability_agent,ceph_management_agent
from tasks import observability_task, management_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[observability_agent, ceph_management_agent],
    tasks=[observability_task, management_task],
    verbose=True,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    process=Process.sequential,  # Optional: Sequential task execution is default
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'Get disk occupation'})
import pdb
pdb.set_trace()
print(result.output)
