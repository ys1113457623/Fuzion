import json
from multiprocessing.resource_sharer import stop
import openai
import requests

from dotenv import load_dotenv
from pathlib import Path
import os


# dotenv_path = Path('./.env')
load_dotenv()
API_TOKEN = os.getenv("HUGGING_FACES")
OPEN_AI_TOKEN = os.getenv("OPEN_AI")
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def imageDescription(request):
    query = request
    print(query)
    API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    response = requests.get(query)
    # data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=query)
    response = response.content.decode("utf-8")
    return response

def questionAnswering(question:str,context:str)->str:
    payload = {
        "inputs": {
            "question": question,
            "context":context,
        }
    }
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

class DavinciTasks:
    
    
    def __init__(self) -> None:
        openai.api_key = OPEN_AI_TOKEN
    
    def name_generator(self,product_description:str):
        prompt = f"""
Product description: A home milkshake maker
Seed words: fast, healthy, compact.
Product names: HomeShaker, Fit Shaker, QuickShake, Shake Maker

Product description: {self.summarizeForSecondGrader(product_description,30)}
Seed words: {self.extractKeywords(product_description)}
Product names:
"""
        response = self.query(prompt)
        return response.replace(
"""Product description: A home milkshake maker
Seed words: fast, healthy, compact.
Product names: HomeShaker, Fit Shaker, QuickShake, Shake Maker""","")
    
    def extract_name_mailing(self,text):
        pre_prompt = f"Extract the name and mailing address from this email:\n{text}\n\nName:"
        return self.query(pre_prompt,max_tokens=64)
        
    def query(self,prompt,temperature=0.9,max_tokens=1550,top_p=1,frequency_penalty=0,presence_penalty=0.6,stop=None)->str:
        if stop:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop
            )
            return response.choices[0].text
        response =openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            ) 
        return response.choices[0].text
    
    def generateCaption(self,image_url):
        description = imageDescription(image_url)
        print(description)
        prompt = f"Generate a list of instagram caption for an image with this description \"{description}\""
        return self.query(prompt)
    
    def correctGrammar(self,text):
        prompt = f"Correct this to standard English:\n\n\"{text}\""
        return self.query(prompt)
    
    def tldr(self,prompt:str):
        text = f"{prompt}\n\nTl;dr"
        return self.query(text,max_tokens=100)

    def summarizeForSecondGrader(self,text,tokens = -1):
        prompt = f"Summarize this text for a second-grade:\n\n\"{text}\""
        if tokens!=-1:
            return self.query(prompt,max_tokens=tokens)
        return self.query(prompt)

    def extractKeywords(self,text):
        prompt = f"Extract keywords from this text:\n\n\"{text}\""
        # print(prompt)
        return self.query(prompt)
      
    def factual_answere_generation(self,prompt:str):
        facts = f"""Q: Who is Batman?

A: Batman is a fictional comic book character.

Q: What is torsalplexity?
A: Nahi Pata bhai

Q: What is Devz9?
A: Nahi Pata bhai

Q: Who is George Lucas?
A: George Lucas is American film director and producer famous for creating Star Wars.

Q: What is the capital of California?
A: Sacramento.

Q: What orbits the Earth?
A: The Moon.

Q: Who is Fred Rickerson?
A: Nahi pata bhai

Q: What is an atom?
A: An atom is a tiny particle that makes up everything.

Q: Who is Alvan Muntz?
A: Nahi pata bhai

Q: What is Kozar-09?
A: Nahi pata bhai

Q: How many moons does Mars have?
A: Two, Phobos and Deimos.

Q: {prompt}
A:
        """
        response:str =  self.query(facts,
                                        temperature=0,
                                        presence_penalty=0.6
                                    )
        
        reply = response.replace("""
        Q: Who is Batman?

A: Batman is a fictional comic book character.

Q: What is torsalplexity?
A: Nahi Pata bhai

Q: What is Devz9?
A: Nahi Pata bhai

Q: Who is George Lucas?
A: George Lucas is American film director and producer famous for creating Star Wars.

Q: What is the capital of California?
A: Sacramento.

Q: What orbits the Earth?
A: The Moon.

Q: Who is Fred Rickerson?
A: Nahi pata bhai

Q: What is an atom?
A: An atom is a tiny particle that makes up everything.

Q: Who is Alvan Muntz?
A: Nahi pata bhai

Q: What is Kozar-09?
A: Nahi pata bhai

Q: How many moons does Mars have?
A: Two, Phobos and Deimos.
        ""","")
        
        return reply.strip('\n')
    
    def ad_copy_creation(self,product_description:str):
        try:
            targetAudience =  questionAnswering(
                question="Where will this ad run on?",
                context=product_description
            )['answer']
        except Exception:
            targetAudience = "Everyone"
            
        try:
                targetPlatform = questionAnswering(
                question="Who is the target audience?",
                context=product_description
            )['answer']
        except Exception:
            targetPlatform = "Social Media"

        ad_copy = f"""Write a creative ad for the following product to run on {targetPlatform} aimed at {targetAudience}:

Product: {product_description}."""

        return self.query(ad_copy,
                          temperature=0.5,
                            frequency_penalty=0,
                            presence_penalty=0,
                            # max_tokens=100
                          )
    

if __name__ == "__main__":
    DT = DavinciTasks()
    product = "Naruto Uzumaki is a twelve-year-old ninja living in the Hidden Leaf Village under harsh ridicule from the villagers, having defaced a monument dedicated to the four Hokage leaders out of a need for acknowledgement. Naruto's teacher Iruka Umino reprimands Naruto for putting graffiti on each face statues, later hearing Naruto's aspirations of becoming Hokage to become respected by the villages. The following day, being held back from graduating the Ninja Academy after a botched clone jutsu, Naruto is tricked by an academy teacher named Mizuki into stealing a scroll containing the secret ninjutsu from the Third Hokage Hiruzen Sarutobi that night. Iruka intercepts Naruto as Mizuki was going to kill the boy and leave the village with the stolen scroll. Mizuki then reveals to Naruto that villagers were ordered not to reveal him as a host to a demon fox called the Nine Tails which devastated their village twelve years ago. Mizuki explains this to be the reasoning Naruto is hated, adding that Iruka's parents were killed by the Nine Tails. But a remorseful Iruka protects Naruto while telling the boy they have a lot in common, spurring Naruto to use the Shadow Clone jutsu he learned from the scroll to overwhelm Mizuki. Soon after Iruka uses Naruto's ability to use shadow clones to justify his graduation from the Ninja Academy."
    # print(DT.ad_copy_creation(product))
    print(DT.generateCaption("https://upload.wikimedia.org/wikipedia/en/3/3b/Narutofirstdvd.jpg"))
     

            
        
        

    
          
