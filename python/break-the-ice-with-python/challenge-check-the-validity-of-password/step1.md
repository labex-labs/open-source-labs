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

## Example

Suppose the following input is supplied to the program:

```bash
ABd1234@1,a F1#,2w3E*,2We3345
```

Then, the output of the program should be:

```bash
ABd1234@1
```

## Hints

- In case of input data being supplied to the program, it should be assumed to be a console input.
- Consider using the `isupper()`, `islower()` and `isnumeric()` methods to determine the kind of character.
