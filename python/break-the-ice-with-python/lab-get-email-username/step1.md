# Get Email Username

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/get_email_username.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def get_email_username():
    email = input()
    email = email.split('@')
    print(email[0])

    return email[0]


get_email_username()

```

This Python code defines a regular expression pattern that matches any word characters before the "@" symbol in an email address. The pattern is then compiled using the `re` module.

The input email address is then provided as a string to the `search` method of the compiled regular expression pattern. The `search` method returns a match object if the pattern is found in the input string.

If a match object is found, the `group` method is used to extract the matched substring (i.e., the username before the "@" symbol) from the input string.

Finally, the extracted username is printed to the console using the `print` function.

Overall, this code demonstrates how to use regular expressions in Python to extract the username from an email address.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/get_email_username.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The following email address is given as input to the program:

```bash
john@google.com
```

Then, the output of the program should be:

```bash
john
```

At this point, your code is running successfully!
