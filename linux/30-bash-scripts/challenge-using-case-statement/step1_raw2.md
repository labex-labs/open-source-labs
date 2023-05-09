# Using Case Statement

## Introduction

Bash is a popular shell used in Linux and Unix operating systems. It provides a powerful command-line interface for users to interact with the system. In this challenge, we will explore the use of the case statement in Bash scripting.

## Problem

You need to write a Bash script that takes user input for their lucky number and outputs a message based on the number entered. If the number entered matches a specific value, the script will output a prize message. If the number entered does not match any of the specific values, the script will output a message to try again next time.

## Requirements

- Create a new file named `case_example.sh`.
- Use the `#!/bin/bash` shebang at the beginning of the script.
- Prompt the user to enter their lucky number.
- Use the case statement to check the value of the user's input.
- If the input matches 101, output "You got 1st prize".
- If the input matches 510, output "You got 2nd prize".
- If the input matches 999, output "You got 3rd prize".
- If the input does not match any of the above values, output "Sorry, try for the next time".

## Solution

```bash
#!/bin/bash

echo "Enter your lucky number"
read n
case $n in
  101)
    echo "You got 1st prize"
    ;;
  510)
    echo "You got 2nd prize"
    ;;
  999)
    echo "You got 3rd prize"
    ;;
  *)
    echo "Sorry, try for the next time"
    ;;
esac
```

## Summary

In this challenge, we learned how to use the case statement in Bash scripting. The case statement provides an alternative to the if-elseif-else statement and can be used to check multiple values of a variable. By using the case statement, we were able to create a script that outputs a message based on the user's input.
