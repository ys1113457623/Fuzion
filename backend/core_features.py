import json
from image.views import imageDescription
from dotenv import load_dotenv
from pathlib import Path
from open_ai.main import GPT3_DaVinci
import os
import requests
from fusion_backend.args import headers

def imageDescription(request):
    query = request
    API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    response = requests.get(query)
    # data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=query)
    response = response.content.decode("utf-8")
    
    return response
class GenerateCaption:
    def __init__(self) -> None:
        self.gpt3 = GPT3_DaVinci()
        
    def generateCaption(self,image_url):
        description = imageDescription(image_url)
        print(description)
        prompt = f"Generate a list of instagram caption for an image with this description \"{description}\""
        return self.gpt3.query(prompt)

class GrammarCorrection:
    def __init__(self) -> None:
        self.gpt3 = GPT3_DaVinci()
        
    def correctGrammer(self,text):
        prompt = f"Correct this to standard English:\n\n\"{text}\""
        return self.gpt3.query(prompt)

class SummarizeForSecondGrader:
    def __init__(self) -> None:
        self.gpt3 = GPT3_DaVinci()
        
    def summarizeForSecondGrader(self,text):
        prompt = f"Summarize this text for a second-grade:\n\n\"{text}\""
        return self.gpt3.query(prompt)
    
class ExtractKeywords:
    def __init__(self) -> None:
        self.gpt3 = GPT3_DaVinci()
    
    def extractKeywords(self,text):
        prompt = f"Extract keywords from this text:\n\n\"{text}\""
        return self.gpt3.query(prompt)

class FactualAnswereGeneration:
    def __init__(self) -> None:
        self.gpt3 = GPT3_DaVinci()
    
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
        response:str =  self.gpt3.query(facts,
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
        
        

if __name__ == "__main__":
    # GC = GenerateCaption()
    # print(GC.generateCaption("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkdjZKeWDMO_o7m48FHwwIC8Gk6XdKigKqQQ&usqp=CAU"))
    # Grammer_Correction = GrammarCorrection()
    # print(Grammer_Correction.correctGrammer("love is she in"))
    # Summarize = SummarizeForSecondGrader()
    # ttext = 
    # print(Summarize.summarizeForSecondGrader(

    # ))
#     EK = ExtractKeywords()
#     teet = """Re: With the current builds, can you switch from RAID to AHCI in Win 11 if the system comes with an SSD and HDD installed?  I don't intend to use the HDD for anything other than backups. I've also installed a second SATA HDD if that makes a difference (where my Linux OSs are installed). If it's possible to boot in AHCI mode, how is it done?

# One option is to do a clean install Win 11 or Win 10 on the stock ssd after bios sata operation is switched to AHCI and pc is restarted to boot from a bootable usb or dvd Win 11/10 installation media, when there is no second ssd or hdd installed.  After install is done then connect the hdd and delete all old partitions in disk mgmt and create a single new partition.  
# For dual boot, I would repeat the same step. Remove the ssd containing Win 11/10 and hdd, keep bios on AHCI, connect the second ssd and do a clean install of OS (Linux etc.).  When done reconnect all drives.  Now at beginning of boot pc will prompt you to pick a boot drive from two that it detects.
#     """
#     print(EK.extractKeywords(text=teet))
#     print(SummarizeForSecondGrader().summarizeForSecondGrader(teet))
    question = "Who is the Prime Minister of Australia"
    FA = FactualAnswereGeneration()
    print(FA.factual_answere_generation(question))
    
    
    
    
        