from .base import ImagePacker
from PIL import Image

class Gray8Packer(ImagePacker):
    @property
    def name(self) -> str:
        return "gray8"

    @property
    def colored(self) -> bool:
        return False

    @property
    def alpha(self) -> bool:
        return True

    def pack(self, image: Image.Image) -> bytes:
        # Alpha stored as the byte value
        # We use the alpha channel directly
        alpha_channel = image.split()[3]
        return alpha_channel.tobytes()
