# Add Two Numbers

## Problem

Create a bash script named `add_numbers.sh` that prompts the user to enter two integer values, and then prints the result of their addition. The script should use double brackets to perform the addition operation.

## Requirements

* Create a bash script named `add_numbers.sh`
* Prompt the user to enter two integer values
* Use double brackets to perform the addition operation
* Print the result of the addition operation

## Solution

The following code can be used to create the `add_numbers.sh` script.

```bash
#!/bin/bash  
echo "Enter first number"  
read x  
echo "Enter second number"  
read y  
(( sum=x+y ))  
echo "The result of addition=$sum"
```

To run the script, execute the following command in the terminal:

```bash
bash add_numbers.sh
```

