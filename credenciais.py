import json

def credenciais():
       f = open('env.json', 'r')
       c = f.read()
       o = json.loads(c)
       
       return o