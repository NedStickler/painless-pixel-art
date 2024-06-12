
import os
from openai import OpenAI
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv("..")
    secret_key = os.getenv("OPEN_AI_KEY")
    client = OpenAI(api_key=secret_key)

    green = "#00FF00"

    response = client.images.generate(model="dall-e-3", prompt=f"a tomato, with a background of a single solid colour, and no shadows cast by the tomato", size="1024x1024", quality="standard", n=1)
    print(response)