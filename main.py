import publisher
import vosk
import pyfirmata2 as  firmata
import pyaudio
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

       while True:
              try:
                     data = stream.read(4096)
                     if recognizer.AcceptWaveform(data):
                            text = recognizer.Result()
                            t = text[14:-3]
                            
                            print(t)
                            obj = {
                                   "message": t
                            }
                                                 
                            if t.strip() != "":
                            
                                   if ligarFn(t):
                                          obj["gpt"] = "NAO"
                                          obj["message"] = "Comando de ligar foi acionado!"
                                          LED_pin.write(False)
                                          
                                   elif desligarFn(t):
                                          obj["gpt"] = "NAO"
                                          obj["message"] = "Comando de desligar foi acionado!"
                                          LED_pin.write(True)

                                   else:
                                          obj["gpt"] = "SIM"
                                   
                                   print(obj)
                                   aa = json.dumps(obj)
                                   publisher.send_message(aa)
                                   
              except Exception as err:
                     q.put("Ocorreu um erro inesperado, o sistema foi reiniciado")
                     print(err)

worker1()