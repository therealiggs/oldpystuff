with open('smartguy.txt') as file:
    text = [line for line in file]

def code(word,key):
    ans = []
    klst = list(key)
    i = 0
    for line in word:
        e=line.encode('cp1251')
        s = []
        for byte in e:
            k = ord(klst[i%len(klst)])
            s += [(byte + k)%256]
            i += 1
        ans+= bytes(s).decode('cp1251')
    return ''.join(i for i in ans) 

def decode(word,key):
    ans = []
    klst = list(key)
    i = 0
    for line in word:
        e=line.encode('cp1251')
        s = []
        for byte in e:
            k = ord(klst[i%len(klst)])
            s += [(byte - k)%256]
            i += 1
        ans+= bytes(s).decode('cp1251')
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
print('Completed')
