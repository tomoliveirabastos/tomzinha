
# from firmata_function import FirmataBoard
# FirmataBoard().ligar('d:7:o')
from vosk import Model, KaldiRecognizer
import pyfirmata2 as  firmata
import pyaudio
import pyttsx3
import json

f = open("env.json")
content = f.read()
j = json.loads(content)

def ligarFn(frase: str):
       words = ["liga", "ligar"]
       for word in words:
              if word == frase.strip():
                     return True

       return False
       
def desligarFn(frase: str):
       words = ["desliga", "desligar"]
       for word in words:
              if word == frase.strip():
                     return True

       return False

mic = pyaudio.PyAudio()
PORT = 'COM5'
board = firmata.Arduino(PORT)

stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192) 
stream.start_stream()

model = Model(j["caminho"])
recognizer = KaldiRecognizer(model, 16000) 

LED_pin = board.get_pin("d:7:o")  # Initialize the pin (d => digital, 13 => Number of the pin, o => output)

while True:

       try:
              data = stream.read(4096)
              if recognizer.AcceptWaveform(data):
                     text = recognizer.Result()
                     t = text[14:-3]

                     print(t)
                     
                     if ligarFn(t):
                            LED_pin.write(False)
              
                     elif desligarFn(t):
                            LED_pin.write(True)
  
       except Exception as err:
              print(err)
                     
                     