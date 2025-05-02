from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from metrics_operations import check_degraded_pgs, check_recent_osd_crashes, get_ceph_daemon_counts, get_cluster_health, get_diskoccupation, get_high_latency_osds
from agno.storage.agent.postgres import PostgresAgentStorage

# DB connection
db_url = 'postgresql://postgres:postgres@localhost:5432/postgres'
storage = PostgresAgentStorage(
    table_name="agent_sessions",
    db_url=db_url,
)

# Define Tools
tools = [
    Tool(name="Get disk occupation", func=get_diskoccupation, description="Fetches the disk occupation per node."),
    Tool(name="Check degraded PGs", func=check_degraded_pgs, description="Checks degraded PGs."),
    Tool(name="Check recent OSD crashes", func=check_recent_osd_crashes, description="Checks recent OSD crashes."),
    Tool(name="Check cluster health", func=get_cluster_health, description="Check cluster health"),
    Tool(name="Check high latency OSDs", func=get_high_latency_osds, description="Check high latency OSDs"),
    Tool(name="Check count of daemons", func=get_ceph_daemon_counts, description="Check count of daemons")
]

agent_prompt = """You are a Ceph observability assistant. Only answer questions related to Ceph cluster status, health, storage, and performance. 
If a query is unrelated to Ceph, respond with: 'I can only assist with Ceph-related queries.'

- If the user asks for **disk occupation** (e.g., "Get disk occupation"), always use `Get disk occupation`.
- If the user asks for **cluster status** (e.g., "What is the status of Cluster 1?"), always use `Check cluster health`.
- If the user asks to **list OSDs**, use `Check count of daemons`.

Do not make assumptions. Only respond with the correct tool.
Do NOT guess. Only respond using the correct tool.
"""

def create_monitoring_agent(llm, memory):    
    agent = initialize_agent(
        storage=storage,
        tools=tools,
        prompt=agent_prompt,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent
