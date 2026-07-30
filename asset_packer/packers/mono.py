from .base import ImagePacker
import numpy as np
from PIL import Image

class MonoPacker(ImagePacker):
    @property
    def name(self) -> str:
        return "mono"

    @property
    def colored(self) -> bool:
        return False

    @property
    def alpha(self) -> bool:
        return False

    def pack(self, image: Image.Image) -> bytes:
        # Alpha ignored, transparent pixels become white
        # We assume image is RGBA
        background = Image.new("RGBA", image.size, (255, 255, 255, 255))
        composite = Image.alpha_composite(background, image)
        
        gray = composite.convert("L")
        bw = gray.point(lambda p: 255 if p > 128 else 0).convert("1")
        
        width, height = bw.size
        pixels = np.array(bw, dtype=np.uint8)
        
        bitmap = []
        bit_offset = 0
        current_byte = 0
        
        # Original code iterated for x then for y. 
        # Usually bitmaps are row-major (y then x), 
        # but I'll stick to original logic if I can find it.
        # Original logic:
        # for x in range(width):
        #     for y in range(height):
        #         if pixels[y, x] == 0:  # Black pixel
        #             bitmap[-1] |= (1 << (7 - bitOffset))
        #         bitOffset += 1
        #         ...
        
        for x in range(width):
            for y in range(height):
                if pixels[y, x] == 0:  # Black pixel
                    current_byte |= (1 << (7 - bit_offset))
                bit_offset += 1
                if bit_offset == 8:
                    bitmap.append(current_byte)
                    current_byte = 0
                    bit_offset = 0
        
        if bit_offset != 0:
            bitmap.append(current_byte)
            
        return bytes(bitmap)
