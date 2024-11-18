from pygame import mixer

class Sound:
    def __init__(self):
        self.channel = mixer.Channel(0)
        self.channel.set_volume(0.2)
        
        self.capture = mixer.Sound("./sfx/capture.mp3")
        self.move = mixer.Sound("./sfx/move.mp3")
    
    def play(self, sound:mixer.Sound) -> None:
        self.channel.play(sound)