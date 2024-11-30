import json
import os

from ..type import *
from .sprite import *

class Sprites:
    def __init__(self, folder_sprites:AnyPath) -> None:
        try:
            with open(os.path.join(folder_sprites, ".json")) as jsonFile:
                sprites = json.load(jsonFile)
        except FileNotFoundError:
            raise Exception("File .json in folder", folder_sprites,"not found.")
        self.SpriteCollection = self.loads(sprites)
    
    def loads(self, sprites:List[dict]) -> dict:
        spriteDict = {}
        for sprite in sprites:
            spriteDict[sprite["id"]] = Sprite.load(sprite["file"])
        return spriteDict

# if __name__ == "__main__":
#     spriteCollection = Sprites("./sprites/piece").SpriteCollection
#     print(spriteCollection)