
from dall_e import DallE
from postprocessing import postprocess
from pathlib import Path
from typing import Literal


class Generator:
    """Generate pixel art using Dall-E 2 and post-processing methods.
    
    Attributes:
        __dall_e: DallE class for generating initial images.
        __post_process_params: Parameter dictionary for changing post-processing settings.
    """
    def __init__(self, api_key: str | None = None) -> None:
        """Initialise Dall-E 2 and post-processing parameters.
        
        Args:
            api_key: OpenAI developer API key. If left as None environment variable 'OPENAI_API_KEY' is used.
        """
        self.__dall_e = DallE(api_key)
        self.__postprocess_params = {
            "save_path": None,
            "dimensions": (32, 32),
            "remove_bg": True,
            "keep_original": True
        }
    
    def generate(self, item: str, save_path: str | Path) -> None:
        """Generate and post-process pixel art.
        
        Args:
            item: Description of a pixel art item to generate. Example: 'a juicy red apple'.
            save_path: Path to save the image(s) to.
        """
        self.__dall_e.create(
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
        """dict: Current state of post-processing parameters."""
        return self.__postprocess_params
    
    def update_postprocess_params(self, update_dict: dict[Literal["save_path", "dimensions", "remove_bg", "keep_original"], any]) -> None:
        """Update post-processing parameters.
        
        Args:
            update_dict: Dictionary of parameters to update. Must be a valid parameter.
        
        Raises:
            KeyError: If any key in `update_dict` is not a valid for `postprocess()`.
        """
        for key in update_dict.keys():
            if key not in self.__postprocess_params:
                raise KeyError(f"No param named {key} to update.")
        self.__postprocess_params.update(update_dict)
