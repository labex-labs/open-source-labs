import re

def get_email_company_name():
    email = input()
    pattern = "\w+@(\w+).com"
    ans = re.findall(pattern, email)
    print(ans)

    return ans

get_email_company_name()
