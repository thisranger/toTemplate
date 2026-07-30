from abc import ABC, abstractmethod
from PIL import Image

class ImagePacker(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def colored(self) -> bool:
        pass

    @property
    @abstractmethod
    def alpha(self) -> bool:
        pass

    @abstractmethod
    def pack(self, image: Image.Image) -> bytes:
        pass
