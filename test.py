with open('smartguy.txt') as file:
    text = [line for line in file]

def code(word,key):
    ans = []
    klst = list(key)
    i = 0
    
    for line in word:
        k = ord(klst[i%len(klst)])
        e=line.encode('cp1251')
        s = bytes([(byte + k)%256 for byte in e])
        ans+= s.decode('cp1251')
        i += 1
    return ''.join(i for i in ans) 

def decode(word,key):
    ans = []
    klist = list(key)
    i = 0
    for line in word:
        k = ord(klst[i%len(klst)])
        e=line.encode('cp1251')
        s = bytes([(byte - k)%256 for byte in e])
        ans+= s.decode('cp1251')
        i += 1
    return ''.join(i for i in ans) 

print('Ключ?')
gkey = input()

with open('smartguy.txt','w') as file:
    flag = False
    while not flag:
        print('Что делать?')
        command = input()
        if 'зашифровать'.startswith(command.lower()):
            for char in code(text,gkey):
                print(char,file=file,end='')
            flag = True
        elif 'расшифровать'.startswith(command.lower()):
            for char in decode(text,gkey):
                print(char,file=file,end='')
            flag = True
        else:
            print('Нет такой команды!')
