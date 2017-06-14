with open('caesar.txt') as file:
    text = [line for line in file]

def code(word,key):
    ans = []
    for line in word:
        e=line.encode('cp1251')
        s = bytes([(byte + key)%256 for byte in e])
        ans+= s.decode('cp1251')   
    return ''.join(i for i in ans) 

def decode(word,key):
    ans = []
    for line in word:
        e=line.encode('cp1251')
        s = bytes([(byte - key)%256 for byte in e])
        ans+= s.decode('cp1251') 
    return ''.join(i for i in ans) 

print('Ключ?')
gkey = int(input())

with open('caesar.txt','w') as file:
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
