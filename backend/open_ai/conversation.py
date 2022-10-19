import openai
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN = os.getenv("HUGGING_FACES")
OPEN_AI_TOKEN = os.getenv("OPEN_AI")
headers = {"Authorization": f"Bearer {API_TOKEN}"}


class DavinciConversation:
    def __init__(self) -> None:
        openai.api_key = OPEN_AI_TOKEN
        self.prompt=""
    
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
    
    def emulate_a_friend(self,prompt:str):
        if self.prompt.count("You")<1:
            self.prompt = f"You: What have you been up to?\nFriend: Watching old movies.\nYou: {prompt}\nFriend: "
        else:
            self.prompt = f"{prompt}\nFriend:"
        return self.query(prompt,
                          temperature=0.5,
                          top_p=1,
                          frequency_penalty=0.5,
                          stop=["You:","Friend:"])
    
    def chat_with_ai(self,prompt:str):
        if self.prompt.count("AI")<1:
            self.prompt = f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?{prompt}\nAI:"
        else:
            self.prompt = f"{prompt}\nAI:"
            
        return self.query(prompt,
                          temperature=0.5,
                          top_p=1,
                          frequency_penalty=0.5,
                          stop=["Human:","AI:"]
                          )

    def sassy_chat(self,prompt:str):

        if "Raj" not in prompt:
            self.prompt=f"Marv is a chatbot that never gives straight answers :\n\nYou:{prompt}\nMarv:"
        else:
            self.prompt = f"{prompt}\Marv:"
        return self.query(prompt,
                          temperature=0.5,
                          top_p=0.3,
                          frequency_penalty=0.5,
                          presence_penalty=0,
                        )

        

if __name__ == "__main__":
    DC = DavinciConversation()
    prompt = "My Wife told me I should do lunges to stay in shame, but I don't want to, Should I do?"
    print(DC.emulate_a_friend(prompt))
    print(DC.chat_with_ai(prompt))
    print(DC.sassy_chat(prompt))