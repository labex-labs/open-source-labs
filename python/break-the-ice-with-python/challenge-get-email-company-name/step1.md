# Get Email Company Name

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

## Example

The following email address is given as input to the program:

```bash
john@google.com
```

Then, the output of the program should be:

```bash
google
```

## Hints

- Use the `input()` function to get the Email address.
- Use \w to match letters.
- Use `re.findall()` to find all substring using regex.
