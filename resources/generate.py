from pathlib import Path
from PIL import Image

ico_sizes = (16, 32, 64, 128, 256, 512)

def generate_ico(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file, sizes=[(size, size) for size in ico_sizes])

def resize_png(input_file, output_file, size):
    img = Image.open(input_file)
    img.thumbnail((size, size))
    img.save(output_file, sizes=size)

def generate_icons(resources_root):
    sources_dir = resources_root / 'icons'
    output_dir = resources_root / 'generated'

    output_dir.mkdir(exist_ok=True)

    generate_ico(sources_dir / 'IconCropped.png', output_dir / 'app.ico')
    generate_ico(sources_dir / 'IconFile.png', output_dir / 'document.ico')

    resize_png(sources_dir / 'IconFull.png', output_dir / 'icon.png', 600)
    resize_png(sources_dir / 'IconCropped.png', output_dir / 'icon_small.png', 176)


def main():
    generate_icons(Path(__file__).resolve().parent)


if __name__ == '__main__':
    main()
