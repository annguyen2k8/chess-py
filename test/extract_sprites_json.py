import os
import json

colors = {
    "b":"black",
    "w":"white"
}

pieces = {
    "B":"bishop",
    "K":"king",
    "N":"knight",
    "R":"rook",
    "Q":"queen",
    "P":"pawn"
}

path_sprites = "./sprites/piece/"

listPieces = []
for filename in os.listdir(path_sprites):
    splitName = os.path.splitext(filename)
    if splitName[-1] not in [".png", ".jpeg"]:
        continue
    color = colors.get(splitName[0][0], splitName[0][0])
    piece = pieces.get(splitName[0][1:], splitName[0][1:])
    listPieces.append({"id":f"{piece}:{color}", "file":os.path.join(path_sprites, filename)})

with open(os.path.join(path_sprites, ".json"), "w") as jsonFile:
    json.dump(listPieces, jsonFile)