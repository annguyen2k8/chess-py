import os
from cairosvg import svg2png

path_svgs = "lila\\public\\piece\\alpha"
path_out = "assets\\piece"

for path in os.listdir(path_svgs):
    name, header = os.path.splitext(path)
    if header == ".svg":
        with open(os.path.join(path_svgs ,path), "r") as f:
            svg2png(f.read(), write_to=os.path.join(path_out, f"{name}.png"), output_height=128, output_width=128)
            print(f"extended {name}.png")