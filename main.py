import vosk
import threading
import pyfirmata2 as  firmata
import pyaudio
import pyttsx3
import json
import queue


q = queue.Queue()

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

def worker1():
       mic = pyaudio.PyAudio()
       PORT = 'COM5'
       board = firmata.Arduino(PORT)
       stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192) 
       stream.start_stream()
       model = vosk.Model(j["caminho"])
       recognizer = vosk.KaldiRecognizer(model, 16000) 
       LED_pin = board.get_pin("d:7:o")  # Initialize the pin (d => digital, 13 => Number of the pin, o => output)

       q.put("Olá, eu sou a Tomzinha")

       while True:
              try:
                     data = stream.read(4096)
                     if recognizer.AcceptWaveform(data):
                            text = recognizer.Result()
                            t = text[14:-3]
                            print(t)
                            
                            if t.strip() != "":
                                   if ligarFn(t):
                                          LED_pin.write(False)
                                          q.put("O comando de ligar foi acionado.")
                                          
                                   elif desligarFn(t):
                                          LED_pin.write(True)
                                          q.put("O comando de desligar foi acionado.")

                                   else:
                                          q.put("Eu não entendi o comando, pode repetir ?")
                                   
              except Exception as err:
                     q.put("Ocorreu um erro inesperado, o sistema foi reiniciado")
                     print(err)
                     
def worker2():
       engine = pyttsx3.init()
       
       while True:
              a = q.get()
              engine.say(a)
              engine.runAndWait()

q.join()

t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()