# Using else if statement

## Introduction

Bash is a popular Unix shell and command language. It is used to automate repetitive tasks, manage system configurations, and execute complex scripts. In this challenge, we will explore how to use the **else if** statement in Bash.

## Problem

The problem is to create a Bash script that uses the **else if** statement to check a user's lucky number and award prizes accordingly. The script should prompt the user to enter their lucky number and then check it against a set of predefined values. If the number matches one of the values, the script should print a message indicating the prize the user has won. If the number does not match any of the values, the script should print a message indicating that the user did not win a prize.

## Requirements

- The script should be named `elseif_example.sh`.
- The script should use the **else if** statement to check the user's lucky number.
- The script should prompt the user to enter their lucky number.
- The script should check the user's lucky number against the following values:
  - 101: 1st prize
  - 510: 2nd prize
  - 999: 3rd prize
- If the user's lucky number matches one of the values, the script should print a message indicating the prize the user has won.
- If the user's lucky number does not match any of the values, the script should print a message indicating that the user did not win a prize.

## Solution

Here is the solution to the problem:

```bash
#!/bin/bash

echo "Enter your lucky number"
read n

if [ $n -eq 101 ];
then
echo "You got 1st prize"
elif [ $n -eq 510 ];
then
echo "You got 2nd prize"
elif [ $n -eq 999 ];
then
echo "You got 3rd prize"
else
echo "Sorry, try for the next time"
fi
```

Save the script as `elseif_example.sh` and run it with the following command:

```bash
bash elseif_example.sh
```

## Summary

In this challenge, we learned how to use the **else if** statement in Bash to check a user's lucky number and award prizes accordingly. We also learned how to prompt the user for input and how to use conditional statements to control the flow of the script. With these skills, we can create more complex Bash scripts to automate tasks and manage system configurations.