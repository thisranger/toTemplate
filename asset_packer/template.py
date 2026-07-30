import os
from jinja2 import Environment, FileSystemLoader
from .assets import Asset, Animation
from typing import List

class TemplateRenderer:
    def __init__(self, template_dir: str):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def render(self, template_name: str, bitmap: bytes, images: List[Asset], animations: List[Animation]) -> str:
        template = self.env.get_template(template_name)
        
        formatted_bitmap = [f"0x{b:02X}" for b in bitmap]
        
        return template.render(
            bitmap=formatted_bitmap,
            images=images,
            animations=animations
        )
