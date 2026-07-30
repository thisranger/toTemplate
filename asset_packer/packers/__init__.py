from .mono import MonoPacker
from .gray8 import Gray8Packer
from .rgb888 import RGB888Packer
from .rgba8888 import RGBA8888Packer

PACKERS = {
    "mono": MonoPacker(),
    "gray8": Gray8Packer(),
    "rgb888": RGB888Packer(),
    "rgba8888": RGBA8888Packer()
}
