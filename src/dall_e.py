
from base64 import b64decode
from openai import OpenAI
from pathlib import Path


class DallE():
    """A wrapper that generates and saves images using Dall-E 2.

    Attributes:
        _client: OpenAI query client.
    """
    def __init__(self, api_key: str | None = None) -> None:
        """Initialises the _client attribute.

        Args:
            api_key: OpenAI developer API key. If left as None environment variable 'OPENAI_API_KEY' is used.
        """
        self._client = OpenAI(api_key=api_key)

    def create(self, prompt: str, save_path: str | Path) -> None:
        """Method for generating and saving images.
        
        Args:
            prompt: String containing the image prompt Dall-E 2 will generate.
            save_path: Path to save the image to.
        """
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
