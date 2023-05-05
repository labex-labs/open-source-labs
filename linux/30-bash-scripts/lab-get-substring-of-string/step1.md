# Get Substring of String

## Problem

The problem is to extract a substring from a given string in Bash. The substring can be of any length and can start from any position in the string.

## Requirements

To solve this problem, we need to follow the below requirements:
- Create a Bash script file with a name of your choice.
- Define a string variable with the desired string value.
- Use the Bash built-in syntax `${string:position:length}` to extract the substring from the string.
- Replace `string` with the name of the string variable, `position` with the starting position of the substring, and `length` with the length of the substring.
- Print the extracted substring using the `echo` command.

## Solution

Here is an example Bash script that demonstrates how to get a substring of a string:

```bash
#!/bin/bash
string="Learn Bash scripting from BashChallenge"
substring=${string:6:4}
echo $substring
```

In this script, we define a string variable `string` with the value "Learn Bash scripting from BashChallenge". We then use the Bash built-in syntax `${string:6:4}` to extract a substring starting from the 6th position and having a length of 4 characters. Finally, we print the extracted substring using the `echo` command.

