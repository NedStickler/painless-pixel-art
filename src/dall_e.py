
import os
from openai import OpenAI
from openai.types import ImagesResponse
from dotenv import load_dotenv


class DallE():
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self._client = OpenAI(api_key=api_key)

    def create(self, prompt: str) -> ImagesResponse:
        response = self._client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response


if __name__ == "__main__":
    load_dotenv("..")
    secret_key = os.getenv("OPEN_AI_KEY")
    dalle = DallE(secret_key)
    response = dalle.create("a tomato")
    print(response)