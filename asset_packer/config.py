import json
import os
from typing import List, Dict, Any

class Config:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.data = json.load(f)
        self.config_dir = os.path.dirname(config_path)

    def get_images(self) -> List[Dict[str, Any]]:
        raw_images = self.data.get("images", [])
        expanded_images = []

        for item in raw_images:
            path = item.get("path")
            if not os.path.isabs(path):
                # path = os.path.join(self.config_dir, path)
                path = os.path.abspath(os.path.join(self.config_dir, path))
            
            if os.path.isdir(path):
                recursive = item.get("recursive", False)
                format_ = item.get("format", "mono")
                
                for root, dirs, files in os.walk(path):
                    if not recursive and root != path:
                        continue
                    for file in files:
                        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                            name = os.path.splitext(file)[0]
                            expanded_images.append({
                                "name": name,
                                "path": os.path.join(root, file),
                                "format": format_
                            })
            else:
                item["path"] = path # update to absolute path
                expanded_images.append(item)
        
        return expanded_images

    def get_animations(self) -> List[Dict[str, Any]]:
        return self.data.get("animations", [])
