from gpt4all import GPT4All
import json

f = open('env.json', 'r')
contents = f.read()
val = json.loads(contents)

m1 = "orca-mini-3b-gguf2-q4_0.gguf"
m2 = "mistral-7b-openorca.Q4_0.gguf"

model = GPT4All(
    model_name=m2,
    model_path=val["ia"],
    allow_download=True
)

def make_question(pergunta):
       print("----> make_question")
       with model.chat_session():
              response = model.generate(prompt=pergunta)
              response1 = ""

              print(response)

              for m in model.current_chat_session:
                     if m["role"] == "assistant":
                            response1 += m["content"] + "\n\n"

              return response1