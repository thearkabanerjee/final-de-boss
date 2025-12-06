# print if a number is prime or not 

number = int (input ('Enter the number : '))
absnumber = abs (number)

counter = 0
for i in range (2, absnumber):
    if (absnumber % i == 0):
        counter += 1
        print (i)
    else :
        continue

if (counter == 0) :
    print ('num is prime')
else :
    print ('num is not prime')