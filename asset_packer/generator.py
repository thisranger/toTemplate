from typing import List, Dict, Any, Tuple
from .assets import Asset, Animation
from .image_loader import load_image
from .packers import PACKERS

class Generator:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}
        self.animations: List[Animation] = []
        self.total_bitmap: bytes = b''

    def process(self, images_cfg: List[Dict[str, Any]], animations_cfg: List[Dict[str, Any]]):
        offset = 0
        
        # Process images first
        for img_cfg in images_cfg:
            name = img_cfg["name"]
            path = img_cfg["path"]
            format_name = img_cfg["format"]
            
            if format_name not in PACKERS:
                raise ValueError(f"Unknown format: {format_name}")
            
            packer = PACKERS[format_name]
            image = load_image(path)
            packed_data = packer.pack(image)
            
            asset = Asset(
                name=name,
                width=image.width,
                height=image.height,
                format=format_name,
                offset=offset,
                data=packed_data,
                colored=packer.colored,
                alpha=packer.alpha
            )
            
            self.assets[name] = asset
            self.total_bitmap += packed_data
            offset += len(packed_data)
            
        # Process animations
        for anim_cfg in animations_cfg:
            frame_names = anim_cfg["frames"]
            frames = []
            for frame_name in frame_names:
                if frame_name not in self.assets:
                    raise ValueError(f"Animation frame {frame_name} not found in images")
                frames.append(self.assets[frame_name])
            
            animation = Animation(
                name=anim_cfg["name"],
                millis_per_frame=anim_cfg["millisPerFrame"],
                auto_start=anim_cfg.get("autoStart", False),
                repeat=anim_cfg.get("repeat", False),
                frames=frames
            )
            self.animations.append(animation)

    def get_result(self) -> Tuple[bytes, List[Asset], List[Animation]]:
        return self.total_bitmap, list(self.assets.values()), self.animations
