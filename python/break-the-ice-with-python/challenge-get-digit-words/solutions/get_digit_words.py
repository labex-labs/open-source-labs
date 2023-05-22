def GetDigitWords():
    words = input().split()
    ans = []
    for word in words:
        if word.isdigit():       # can also use isnumeric() / isdecimal() function instead
            ans.append(word)
    print(ans)

    return ans


GetDigitWords()
