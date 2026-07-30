from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Asset:
    name: str
    width: int
    height: int
    format: str
    offset: int
    data: bytes
    colored: bool
    alpha: bool

@dataclass
class Animation:
    name: str
    millis_per_frame: int
    auto_start: bool
    repeat: bool
    frames: List[Asset]
    amount_of_frames: int = 0

    def __post_init__(self):
        self.amount_of_frames = len(self.frames)
