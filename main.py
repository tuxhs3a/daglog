import os
import random

running = True

path_logs = r".\logs"
chars = (
    "0123456789"
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ"
    "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝŸ"
    "āăąćčďđēėęěğīįıĺľłńňōőŕřśšşťţūůűųŵźżž"
    "ĀĂĄĆČĎĐĒĖĘĚĞĪĮİĹĽŁŃŇŌŐŔŘŚŠŞŤŢŪŮŰŲŴŹŻŽ"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿"
    "×÷€ "
)

random.seed(610202620233)

chars = list(chars)
random.shuffle(chars)
chars = "".join(chars)
len_chars = len(chars)

def trans(txt,key):
    new_txt = ""
    
    for char in txt:
        pos = chars.find(char)
        
        if pos:
            new_key = (pos + key) % len_chars
            
            new_txt += chars[new_key]
        else:
            new_txt += char
        
    return new_txt

def make_log(name,txt):
    path_log = os.path.join(path_logs,f"{name}.daglog")
    key = int(input())
    
    if key != "no":
        txt = trans(txt,key)
    
    with open(path_log,"x",encoding='utf-8') as log:
        log.write(txt.replace("\\n","\n"))
        
        return 1

def read_log(name):
    path_log = os.path.join(path_logs,f"{name}.daglog")
    
    with open(path_log,encoding='utf-8') as log:
        return log.read()

while running:
    cmd = input()
    
    if cmd == "quit":
        running = False
    
    if cmd == "mklog":
        name = input()
        txt = input()
        
        result = make_log(name,txt)
        
        if result:
            print(result)
            
    if cmd == "rdlog":
        name = input()
        
        txt = read_log(name)
        key = int(input())
        
        if key != "no":
            txt = trans(txt,key)
            
        print(txt)
        
        