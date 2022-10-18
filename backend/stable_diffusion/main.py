from typing import List
import replicate 

class StableDiffusion:
    def __init__(self) -> None:
        self.model = replicate.models.get("stability-ai/stable-diffusion")

    def make_image(self, text:str,prompts_strength:int=0.8,num_outputs: int=1,) -> List[str]:
        print(text)
        return self.model.predict(prompt=text,num_outputs=num_outputs,prompts_strength=prompts_strength)

class DalleMini:
    def __init__(self) -> None:
        self.model  = replicate.models.get("borisdayma/dalle-mini")
        
    def make_image(self, text:str,) -> List[str]:
        return self.model.predict(prompt=text,n_predictions=1)
    

if __name__ == "__main__":
    sd = StableDiffusion()
    dm = DalleMini()
    prompt = "a majestic tower in a field of flowers landscape by"
    res2 = dm.make_image(prompt)
    res = sd.make_image(prompt)
    print(res)
    print()
    print(res2)

