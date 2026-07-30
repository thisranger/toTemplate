import sys
import os
from asset_packer.config import Config
from asset_packer.generator import Generator
from asset_packer.template import TemplateRenderer

def main():
    if len(sys.argv) < 4:
        print(f"Usage: python -m asset_packer.main <config.json> <output_dir> <template_name_1> [template_name_2 ...]")
        print("Example: python -m asset_packer.main config.json output images.h.j2 images.c.j2")
        sys.exit(1)

    config_path = sys.argv[1]
    output_dir = sys.argv[2]
    template_names = sys.argv[3:]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load config
    config = Config(config_path)
    images_cfg = config.get_images()
    animations_cfg = config.get_animations()

    # Process assets
    generator = Generator()
    generator.process(images_cfg, animations_cfg)
    bitmap, images, animations = generator.get_result()

    # Render templates
    # We assume templates are in the package's templates folder or absolute path
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    renderer = TemplateRenderer(template_dir)

    for template_name in template_names:
        output_content = renderer.render(template_name, bitmap, images, animations)
        
        # Determine output filename: remove .j2 extension
        out_filename = template_name
        if out_filename.endswith('.j2'):
            out_filename = out_filename[:-3]
        
        out_path = os.path.join(output_dir, out_filename)
        with open(out_path, 'w') as f:
            f.write(output_content)
        print(f"Generated {out_path}")

if __name__ == "__main__":
    main()
