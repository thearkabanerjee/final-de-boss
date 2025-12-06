# reverse the digits in the given number

number : int = int (input ('enter the number: '))
stringofnumber : str = str (number)


reversedstring : str = stringofnumber[::-1]

intstring : int = int(reversedstring)
print (intstring, type(intstring))
print (reversedstring, type(reversedstring))