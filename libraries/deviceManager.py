import pygame
import pygame._sdl2.audio as sdl2_audio

class AudioManager:

    __py_game_init = None
    
    def __init__(self, deviceName: str) -> None:
        if (not self.__isWorkingDevice(deviceName)):
            raise NameError("The configured device not fount in the system")
        
        self.__py_game_init = pygame.mixer.init(devicename=deviceName)

    def __isWorkingDevice(self, deviceName: str):
        pygame.mixer.init()
        devices = tuple(sdl2_audio.get_audio_device_names(False))
        pygame.mixer.quit()
        return deviceName in devices

    def isAudioDeviceBusy(self):
        return pygame.mixer.get_busy()
    
    def playAudio(self, sound):
        pygame.mixer.music.load(sound, "mp3")
        pygame.mixer.music.play()

    def stopManager(self):
        if self.__py_game_init:
            pygame.mixer.quit()