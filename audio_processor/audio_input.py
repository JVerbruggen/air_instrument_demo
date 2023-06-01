from abc import ABC
from abc import abstractmethod
import pyautogui
import utils

class AudioInputController(ABC):
    @abstractmethod
    def get_volume(self):
        ...
    
    @abstractmethod
    def get_pitch(self):
        ...

class MouseXYAudioInputController(AudioInputController):
    def __init__(self):
        self.minX = 0
        self.minY = 0
        self.maxX, self.maxY = pyautogui.size()
        self.minPitch = 300
        self.maxPitch = 2000
        self.deltaPitch = self.maxPitch - self.minPitch

    def get_volume(self):
        volume = pyautogui.position()[1] / self.maxY
        if volume < 0: volume = 0
        elif volume > 1: volume = 1

        return volume

    def get_pitch(self):
        pitch = utils.lerp(self.minX, self.maxX, self.minPitch, self.maxPitch, pyautogui.position()[0])
        if pitch < self.minPitch: pitch = self.minPitch
        elif pitch > self.maxPitch: pitch = self.maxPitch

        return pitch
