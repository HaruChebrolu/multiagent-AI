from crewai import Task
from agents import observability_agent,ceph_management_agent
from tools import GetDiskOccupationTool


observability_task = Task(
    description="Get {disk occupation} for all nodes in the cluster",
    expected_output="A detailed summary of disk usage per node.",
    agent=observability_agent,
    tools=[GetDiskOccupationTool],
    human_input=True
)

management_task = Task(
    description="Fetches the health status of a Ceph cluster",
    expected_output="A detailed summary of health status per ceph cluster.",
    agent=ceph_management_agent,
    tools=[],
    human_input=True
)