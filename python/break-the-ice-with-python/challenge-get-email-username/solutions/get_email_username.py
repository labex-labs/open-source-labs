def get_email_username():
    email = input()
    email = email.split('@')
    print(email[0])

    return email[0]


get_email_username()
