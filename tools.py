import json
from Observability.metrics_operations import get_diskoccupation

from crewai.tools import tool
	
@tool("GetDiskOccupationTool")
def GetDiskOccupationTool(param_topic: str) -> str:
    """Get Disk Occupation Status"""
    print("Get Disk Occupation function called")
    import pdb
    pdb.set_trace()
    result = get_diskoccupation(param_topic)
    return result

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


# import json
# from Observability.metrics_operations import get_diskoccupation
# from crewai_tools import BaseTool

# class GetDiskOccupationTool(BaseTool):
#     name = "GetDiskOccupationTool"
#     description = "Returns disk usage information for each node in the cluster."

#     def _run(self, **kwargs):
#         disk_data = get_diskoccupation(**kwargs)
#         return json.dumps({"node_disk_usage": disk_data})


