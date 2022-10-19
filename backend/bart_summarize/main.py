import requests
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
hugging_faces = os.getenv("hugging-faces")

class BartLargeCNN:
    def __init__(self) -> None:
        self.API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.headers = {"Authorization":hugging_faces }

    def query(self,payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        reply= response.json()[0]
        return reply
        
        

if __name__ == "__main__":
    BLC = BartLargeCNN()
    
    output = BLC.query({
        "inputs": "If an environment variable is not found in the .env file, load_dotenv will then search for a variable by the given name in the host environment. This means that when your project is running locally and the .env file is present, the variables defined in the file will be used. When your project is deployed to a host environment like a virtual machine or Docker container where the .env file is not present, the environment variables defined in the host environment will be used instead. By default load_dotenv will look for the .env file in the current working directory or any parent directories however you can also specify the path if your particular use case requires it be stored elsewhere.",
    })
    print(output)