# while loops for printing namws 

name : str = str (input('Enter your name: '))
while (name == ''):
    print ('you didnt enter your name')
    name : str = str (input ('Enter your name: '))
print (f'Hello, {name}')