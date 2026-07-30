from .base import ImagePacker
from PIL import Image

class RGBA8888Packer(ImagePacker):
    @property
    def name(self) -> str:
        return "rgba8888"

    @property
    def colored(self) -> bool:
        return True

    @property
    def alpha(self) -> bool:
        return True

    def pack(self, image: Image.Image) -> bytes:
        # Alpha preserved
        return image.tobytes()
