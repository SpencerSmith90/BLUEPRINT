from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from drawing_generator import generate_deck_drawing
import os
import time

app = FastAPI()
app.mount("/drawings", StaticFiles(directory="public/drawings"), name="drawings")

@app.post("/generate-drawing")
async def generate(request: Request):
    data = await request.json()
    timestamp = int(time.time())
    base = f"deck_{timestamp}"
    dxf_path, png_path = generate_deck_drawing(data, base)
    host = os.getenv("RENDER_EXTERNAL_URL", "http://localhost:10000")
    return {
        "dxf_url": f"{host}/drawings/{os.path.basename(dxf_path)}",
        "png_url": f"{host}/drawings/{os.path.basename(png_path)}",
        "details": data
    }
