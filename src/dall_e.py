
from openai import OpenAI
from openai.types import ImagesResponse
from dotenv import load_dotenv


class DallE():
    def __init__(self, api_key: str | None = None) -> None:
        self._client = OpenAI(api_key=api_key)

    def create(self, prompt: str) -> ImagesResponse:
        response = self._client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response


if __name__ == "__main__":
    load_dotenv("..")
    dalle = DallE()
    response = dalle.create("Generate a realistic pickaxe. Do not draw any shadows. Do not add any additional frills to the image. Ensure the object is completely within the image bounds. Make the background colour a perfect white.")
    print(response)