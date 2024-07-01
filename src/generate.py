
from dall_e import DallE
from postprocessing import postprocess
from pathlib import Path
from dotenv import load_dotenv


class Generator:
    def __init__(self, api_key: str | None = None) -> None:
        self.dall_e = DallE(api_key)
    
    def generate(self, item: str, save_path: str | Path) -> None:
        self.dall_e.create(
            f"""Generate a realistic {item}.
            Do not draw any shadows.
            Do not add any additional frills to the image.
            Ensure the object is completely within the image bounds.
            Make the background colour a perfect white.
            """,
            save_path
        )
        postprocess(save_path, keep_original=False)


if __name__ == "__main__":
    load_dotenv("..")
    generator = Generator()
    generator.generate("dog", r".\assets\test_item.png")