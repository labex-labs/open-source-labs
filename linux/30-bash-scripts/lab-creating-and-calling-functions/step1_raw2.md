# Creating and Calling Functions

## Introduction

Bash is a powerful scripting language that allows you to automate tasks and create complex scripts. One of the key features of Bash is the ability to create and call functions. In this challenge, you will learn how to create and call functions in Bash.

## Problem

You have been tasked with creating a Bash script that contains a function. The function should output a message to the console. You need to create the function and call it from within the script.

## Requirements

- The script should be named `function_example.sh`.
- The function should be named `F1`.
- The function should output the message "I like bash programming".
- The function should be called from within the script.
- The script should be run using the `bash` command.

## Solution

To create the function, open a new file named `function_example.sh` and add the following code:

```bash
#!/bin/bash  
function F1()  
{  
echo 'I like bash programming'  
}  
  
F1
```

Save the file and run it using the `bash` command:

```bash
bash function_example.sh
```

The output should be:

```bash
I like bash programming
```

## Summary

In this challenge, you learned how to create and call functions in Bash. By following the requirements and solution, you were able to create a Bash script that contains a function and outputs a message to the console. With this knowledge, you can now create more complex scripts that automate tasks and perform more advanced operations.