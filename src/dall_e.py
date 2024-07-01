
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
            