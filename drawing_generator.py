import ezdxf
from PIL import Image, ImageDraw

def generate_deck_drawing(data, base_filename):
    length = data.get("length_ft", 20)
    width = data.get("width_ft", 10)
    dxf = ezdxf.new()
    msp = dxf.modelspace()
    msp.add_lwpolyline([(0,0), (length,0), (length,width), (0,width)], close=True)
    dxf_path = f"public/drawings/{base_filename}.dxf"
    dxf.saveas(dxf_path)

    size_px = (int(length*10), int(width*10))
    img = Image.new("RGB", size_px, "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,size_px[0]-1,size_px[1]-1], outline="black")
    png_path = f"public/drawings/{base_filename}.png"
    img.save(png_path)
    return dxf_path, png_path
