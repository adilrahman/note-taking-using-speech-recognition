import speech_recognition as sr
import gtts
from playsound import playsound
import os
import time

r = sr.Recognizer()


class SpeechTextEngine:

    def __init__(self) -> None:

        ## Wake up commands
        self.ACTIVATION_COMMAND = [
            "hey friday", "hi friday", "are you there friday", "friday",
            "turn on", "are you there"
        ]

    def get_audio(self):
        with sr.Microphone() as src:
            print("Say...........")
            audio = r.listen(src, phrase_time_limit=5)
            print("audio recognized")

        return audio

    def audio_to_text(self, audio):
        text = ""

        try:
            text = r.recognize_google(audio).lower()
            print(f"\nrecognized text :- {text}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("request error")

        return text

    def speech_recognition(self):
        audio = self.get_audio()
        text = self.audio_to_text(audio=audio)

        return text

    def wakeup(self):
        if self.speech_recognition() in self.ACTIVATION_COMMAND:
            return True
        return False

    def speak(self, text):
        try:
            tts = gtts.gTTS(text)
            temp = "./temp.mp3"
            tts.save(temp)
            playsound(temp)
            os.remove(temp)
        except AssertionError:
            print("could not play sound")


if __name__ == "__main__":

    spr = SpeechTextEngine()

    while True:
        if spr.wakeup():
            print("Activate")
            spr.speak("Activating")
            spr.speak("listening sir")
            time.sleep(1.5)
            while True:
                command = spr.speech_recognition()
                if "deactivate" in command:
                    print("Deactivate!")
                    spr.speak("Deactivating")
                    break
                else:
                    spr.speak("you said :- " + command)
