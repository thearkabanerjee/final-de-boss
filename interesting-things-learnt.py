number = int (input ('enter the number: '))
for i in range (1, 11):
    print ('{0} * {1} = {2}'. format(number, i, number* i))

# another way of writing the same thing
number = int (input ('enter the number: '))
for i in range (1, 11):
    print ('%d x %d = %d'%(number, i, number * i))


# for floats you do like this 

