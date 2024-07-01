
from base64 import b64decode
from openai import OpenAI
from openai.types import ImagesResponse
from dotenv import load_dotenv


class DallE():
    def __init__(self, api_key: str | None = None) -> None:
        self._client = OpenAI(api_key=api_key)

    def create(self, prompt: str, save_path: str) -> None:
        response = self._client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            response_format="b64_json",
            size="1024x1024",
            quality="standard",
            n=1
        )
        img = b64decode(response.data[0].b64_json)
        with open(save_path, "wb") as f:
            f.write(img)

if __name__ == "__main__":
    load_dotenv("..")
    dall_e = DallE()

    prompt = "Generate a realistic pickaxe. Do not draw any shadows. Do not add any additional frills to the image. Ensure the object is completely within the image bounds. Make the background colour a perfect white."
    save_path = r".\assets\pickaxe.png"
    dall_e.create(prompt, save_path)