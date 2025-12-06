def ispalindrome(number: int):
    strnumber = str (number)
    reversed_num = strnumber [::-1]
    intreversed = int(reversed_num)

    if (number == intreversed):
        return ('Palindrome !')
    else:
        return ('Non-Palindrome !')