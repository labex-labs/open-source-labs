def GetEmailUsername():
    email = input()
    email = email.split('@')
    print(email[0])

    return email[0]


GetEmailUsername()
