def ispalindrome(number: int):
    absnumber = abs(number)
    strnumber = str (absnumber)
    reversed_num = strnumber [::-1]
    intreversed = int(reversed_num)

    if (absnumber == intreversed):
        return ('Palindrome !')
    else:
        return ('Non-Palindrome !')
    

whatever: int = ispalindrome(int (input()))
print (whatever)