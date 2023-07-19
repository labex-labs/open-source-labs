# Get Email Company Name

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/get_email_company_name.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import re

def get_email_company_name():
    email = input()
    pattern = "\w+@(\w+).com"
    ans = re.findall(pattern, email)
    print(ans)

    return ans

get_email_company_name()

```

This Python code defines a function called `get_email_company_name`. Within the function, the user is prompted to input an email address.

A regular expression pattern is then defined using the `re` module. The pattern matches any word characters before the "@" symbol, followed by the company name (which is assumed to end with ".com").

The `findall` method of the `re` module is then used to search the input email address for all occurrences of the pattern. The resulting matches are stored in the variable `ans`.

Finally, the resulting matches (i.e., the company names) are printed to the console using the `print` function, and also returned from the function.

Overall, this code demonstrates how to use regular expressions in Python to extract the company name from an email address entered by the user.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/get_email_company_name.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The following email address is given as input to the program:

```bash
john@google.com
```

Then, the output of the program should be:

```bash
google
```

At this point, your code is running successfully!
