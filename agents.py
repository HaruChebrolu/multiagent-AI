from crewai import Agent, LLM
from langchain_community.llms import Ollama
from litellm import completion

from dotenv import load_dotenv
from tools import GetDiskOccupationTool

load_dotenv()

import os

# if we want to use local models with Ollama
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "ollama/llama3.2"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434"
llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434")


# if we want to use groq
# os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
# GROQ_API_KEY = "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"
# os.environ["OPENAI_API_KEY"] = GROQ_API_KEY
# os.environ["OPENAI_MODEL_NAME"] = "llama3-70b"

response = completion(
    model="ollama/llama3.2",
    messages=[{"content": "Hello!", "role": "user"}],
    api_base="http://localhost:11434"
)


import litellm
from litellm import CustomLLM, completion, get_llm_provider


class MyCustomLLM(CustomLLM):
    def completion(self, *args, **kwargs) -> litellm.ModelResponse:           
        import requests

        #print(kwargs["messages"])
        message=kwargs["messages"]

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={WATSONX_APIKEY}'

        response = requests.post('https://iam.cloud.ibm.com/identity/token', headers=headers, data=data).json()["access_token"]
        #print(response)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {response}',
        }

        params = {
            'version': '2023-05-29',
        }

        json_data = {
            'input': f'{message}',
            'parameters': {
                'decoding_method': 'greedy',
                'max_new_tokens': 10000,
                'min_new_tokens': 0,
                'stop_sequences': ['\nObservation: '],
                'stream': False,
                'repetition_penalty': 1,
            },
        }

        response = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v1/deployments/c05b235d-27eb-4140-8f5d-9e8e7520d48d/text/generation',
            params=params,
            headers=headers,
            json=json_data,
        )


        import json


        #myclass4.find={"find": myclass3}

        myclass3.content=str(response.json()["results"][0]["generated_text"]).split("</think>")[1].strip()

        myclass2.message=myclass3

        
        myclass.choices=[myclass2]



    
        return myclass

my_custom_llm = MyCustomLLM()

litellm.custom_provider_map = [ # 👈 KEY STEP - REGISTER HANDLER
        {"provider": "ollama", "custom_handler": my_custom_llm}
    ]



## Create a ceph observability agent
observability_agent=Agent(
    role='Observer from Ceph metrics',
    goal='get the relevant suggestions based on ceph cluster metrics',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding metrics inside Ceph Cluster and providing suggestion" 
    ),
    tools=[GetDiskOccupationTool],
    llm=llm,
    allow_delegation=True
)

# creating a visualization agent
ceph_management_agent=Agent(
    role='Ceph Manager',
    goal='Efficiently manage and respond to all Ceph cluster-related queries',
    verbose=True,
    memory=True,
    backstory=(
        "You are an AI operator responsible for executing tasks on Ceph clusters" 
        "and returning detailed, structured summaries of results"
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)