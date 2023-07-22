# Check the Validity of Password

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

- **_At least 1 letter between [a-z]_**
- **_At least 1 number between [0-9]_**
- **_At least 1 letter between [A-Z]_**
- **_At least 1 character from [$#@]_**
- **_Minimum length of transaction password: 6_**
- **_Maximum length of transaction password: 12_**

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/check_the_validity_of_password.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def check(x):
    cnt = (6 <= len(x) and len(x) <= 12)
    for i in x:
        if i.isupper():
            cnt += 1
            break
    for i in x:
        if i.islower():
            cnt += 1
            break
    for i in x:
        if i.isnumeric():
            cnt += 1
            break
    for i in x:
        if i == '@' or i == '#' or i == '$':
            cnt += 1
            break
    # counting if total 5 all conditions are fulfilled then returns True
    return cnt == 5


s = input().split(',')
# Filter function pick the words from s, those returns True by check() function
lst = filter(check, s)
print(",".join(lst))

```

This Python code implements a function called `check` that checks whether a given string meets the requirements for a password. It uses four loops to check whether the string contains uppercase letters, lowercase letters, numbers, and special characters. If the string meets all the requirements, it returns `True`; otherwise, it returns `False`. The code also uses the `filter` function to select the strings from a user inputted list that meet the requirements and prints them to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/check_the_validity_of_password.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
ABd1234@1,a F1#,2w3E*,2We3345
```

Then, the output of the program should be:

```bash
ABd1234@1
```

At this point, your code is running successfully!
