from .base import ImagePacker
from PIL import Image

class RGB888Packer(ImagePacker):
    @property
    def name(self) -> str:
        return "rgb888"

    @property
    def colored(self) -> bool:
        return True

    @property
    def alpha(self) -> bool:
        return False

    def pack(self, image: Image.Image) -> bytes:
        # Alpha discarded
        rgb_image = image.convert("RGB")
        return rgb_image.tobytes()
