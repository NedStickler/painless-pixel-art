
from dall_e import DallE
from postprocessing import postprocess
from pathlib import Path


class Generator:
    def __init__(self, api_key: str | None = None) -> None:
        self.dall_e = DallE(api_key)
        self.__postprocess_params = {
            "save_path": None,
            "dimensions": (32, 32),
            "remove_bg": True,
            "keep_original": True
        }
    
    def generate(self, item: str, save_path: str | Path) -> None:
        self.dall_e.create(
            f"""Generate {item}.
            Do not draw any shadows.
            Do not add any additional frills to the image.
            Ensure the object is completely within the image bounds.
            Make the background colour a perfect white.
            """,
            save_path
        )
        postprocess(save_path, **self.__postprocess_params)
    
    @property
    def postprocess_params(self) -> dict:
        return self.__postprocess_params
    
    @postprocess_params.setter
    def postprocess_params(self, update_dict: dict) -> None:
        for key in update_dict.keys():
            if key not in self.__postprocess_params:
                raise KeyError(f"No param named {key} to update.")
        self.__postprocess_params.update(update_dict)
        