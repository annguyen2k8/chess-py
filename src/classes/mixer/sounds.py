from pygame.mixer import Sound

class Sounds:
    capture:Sound
    def __init__(self):
        self.capture = Sound("./assets/sfx/capture.mp3")
        self.move = Sound("./assets/sfx/move.mp3")