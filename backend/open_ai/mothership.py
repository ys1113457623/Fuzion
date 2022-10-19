import json
import os
from typing import Any, Dict, List
import requests
from dotenv import load_dotenv
from open_ai.main import DavinciTasks
from open_ai.conversation import DavinciConversation
from ..stable_diffusion.main import StableDiffusion
load_dotenv()
API_TOKEN = os.getenv("HUGGING_FACES")
OPEN_AI_TOKEN = os.getenv("OPEN_AI")
headers = {"Authorization": f"Bearer {API_TOKEN}"}
class MotherShip:


    def query(self,payload:Dict[str,Dict[str,List[str]|str]])->Dict[str,Any]:
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    
    def zero_shot_classification(self,prompt:str,labels)->Dict[str,Any]:
        query = {
            "inputs":prompt,
            "parameters": {"candidate_labels":labels}
        }
        return self.query(query)
    
    def general_passing(self,text:Dict[str]):
        labels = ["create social media captions from image","correct grammar","summarize for second grader","extract keywords","to the point answere generation","generate product name","Generate Image","create ad copy","chatting","General Query about anything"]
        result = self.zero_shot_classification(text['query'],labels)
        if not result :
            return None
        tasks = ["create social media captions from image", "correct grammar", "summarize for second grader", "extract keywords", "to the point answere generation", "generate product name", "create ad copy", "General Query about anything"]
        result = result['labels'][0]
        if result in tasks:
            gpt3 = DavinciTasks()
            if result == "create social media captions from image":
                return gpt3.generateCaption(text['link']),result
            elif result == "correct grammar":
                return gpt3.correctGrammar(text['query']),result
            elif result == "summarize for second grader":
                return gpt3.summarizeForSecondGrader(text['query'],30),result
            elif result == "extract keywords":
                return gpt3.extractKeywords(text['query']),result
            elif result == "to the point answere generation":
                return gpt3.factual_answere_generation(text['query']),result
            elif result == "generate product name":
                return gpt3.name_generator(text['query']),result
            elif result == "extract name and mailing address":
                return gpt3.extract_name_mailing(text['query']),result
            elif result == "create ad copy":
                return gpt3.ad_copy_creation(text['query']),result
            else:
                return gpt3.query(text['query']),result
        elif result == "chatting":
            res:str = self.zero_shot_classification(text['query'],["Conversation with a bot","Conversation with a human"])['labels'][0]
            gpt3Conversation = DavinciConversation()
            if res=="Conversation with a bot":
                return gpt3Conversation.conversation_with_bot(text['query']),result
            else:
                return gpt3Conversation.emulate_a_friend(text['query']),result
        else:
            res =StableDiffusion().make_image(text['query'])
            return res,result
            
            
            
            
        
# MS = MotherShip()
# print(MS.general_passing("I want to create social media captions from image"))