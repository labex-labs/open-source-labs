# Using if Statement with OR Logic

## Introduction

In this challenge, we will learn how to use the OR logic in the if statement of Bash.

## Problem

Create a Bash script named `if_with_OR.sh` that takes a number input from the user. If the value is equal to 15 or 45, then the output will be "You won the game". Otherwise, the output will be "You lost the game".

## Requirements

- Bash shell
- Text editor

## Solution

Use the following code in the `if_with_OR.sh` file:

```bash
#!/bin/bash

echo "Enter any number"
read n

if [[ ($n -eq 15 || $n -eq 45) ]]; then
  echo "You won the game"
else
  echo "You lost the game"
fi
```

Save the file and run it with the following command:

```bash
bash if_with_OR.sh
```

## Summary

In this challenge, we learned how to use the OR logic in the if statement of Bash. We created a Bash script that takes a number input from the user and checks if it is equal to 15 or 45. If it is, then the output is "You won the game". Otherwise, the output is "You lost the game".
