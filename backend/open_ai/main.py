import json
import openai
import requests
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def imageDescription(request):
    query = request
    API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
    response = requests.get(query)
    # data = Image.open(BytesIO(response.content))
    
        
    response = requests.request("POST", API_URL, headers=headers, data=query)
    response = response.content.decode("utf-8")

def questionAnswering(question,context):
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

class GPT3_DaVinci:
    def __init__(self) -> None:
        # load_dotenv(dotenv_path=Path('./.env'))
        
        openai.api_key = "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"
    
    
    
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
        
    def query(self,prompt,temperature=0.9,max_tokens=1550,top_p=1,frequency_penalty=0,presence_penalty=0.6)->str:
        response = openai.Completion.create(
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

        
    def summarizeForSecondGrader(self,text,tokens = -1):
        prompt = f"Summarize this text for a second-grade:\n\n\"{text}\""
        if tokens!=-1:
            return self.query(prompt,max_tokens=tokens)
        return self.query(prompt)

    def extractKeywords(self,text):
        prompt = f"Extract keywords from this text:\n\n\"{text}\""
        # print(kk)
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
        targetPlatform = questionAnswering(
        question="Where will this ad run on?",
        context=product_description
    )
        targetAudience = questionAnswering(
        question="Who is the target audience?",
        context=product_description
    )
        try:
            targetAudience = targetAudience['answer']
        except:
            targetAudience = "Everyone"
        try:
            targetPlatform = targetPlatform['answer']
        except:
            targetPlatform = "Social Media"

        ad_copy = f"""Write a creative ad for the following product to run on {targetPlatform} aimed at {targetAudience}:

Product: {product_description}."""

        return self.query(ad_copy,
                          temperature=0.5,
                            frequency_penalty=0,
                            presence_penalty=0,
                            # max_tokens=100
                          )
        
        

    
          
# Load your API key from an environment variable or secret management service

if __name__ == "__main__":
    # gpt3 = GPT3_DaVinci()
    # print(gpt3.query('Generate a list of insta caption for an image with this description "two men in suits posing for a picture"'))
    context = "A smart assistant that gives the general public their taste of first state of general purpose AI, either by text or voice. That goes beyond Siri and Alexa. and gives you the feel of talking to a really smart and handy person and rather than robot"
    gpt3 = GPT3_DaVinci()
    # print(gpt3.ad_copy_creation(context))
    product_description = "This is a Proudly Indian and 100% PeTA approved Vegan product from Zouk. It has a stylish print inspired by India's rich heritage. It has sturdy and durable accessories, with a zip closure and double straps (non-adjustable). The bag contains a single main compartment. This compartment has an inner padded laptop compartment that can fit up to a 15.6 inch laptop. The compartment also has an inbuilt phone, keychain and pen slot."
    
    print(gpt3.name_generator(product_description))