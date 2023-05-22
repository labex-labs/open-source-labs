import re

def GetEmailCompanyName():
    email = input()
    pattern = "\w+@(\w+).com"
    ans = re.findall(pattern, email)
    print(ans)

    return ans

GetEmailCompanyName()
