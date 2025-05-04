from crewai import Task
from agents import observability_agent
from tools import GetDiskOccupationTool
from pydantic import BaseModel
from typing import List

class ObservabilityModel(BaseModel):
    diskoccupation: List[str] = []

observability_task = Task(
    description="{topic} for all nodes in the cluster",
    expected_output="A detailed summary of disk usage per node.",
    agent=observability_agent,
    tools=[GetDiskOccupationTool],
    output_json=ObservabilityModel
)

# Accessing the task output
task_output = observability_task.output

# import pdb
# pdb.set_trace()
# print(f"Task Description: {task_output.description}")
# print(f"Task Summary: {task_output.summary}")
# print(f"Raw Output: {task_output.raw}")
# if task_output.json_dict:
#     print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
# if task_output.pydantic:
#     print(f"Pydantic Output: {task_output.pydantic}")
