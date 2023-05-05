# Using For Loop

## Problem

Create a Bash script named 'for_example.sh' that uses a 'for' loop to iterate ten times and print each value of the 'counter' variable on a single line.

## Requirements

To successfully complete this challenge, the script should:

* Use a 'for' loop that iterates ten times
* Declare a 'counter' variable that starts at 10 and decrements by 1 with each iteration
* Print each value of the 'counter' variable on a single line, separated by spaces

## Solution

The following code can be used to create the 'for_example.sh' script.

```bash
#!/bin/bash
for (( counter=10; counter>0; counter-- ))
do
    echo -n "$counter "
done
printf "\\n"
```

To run the script, execute the following command in the terminal:
```bash
$ bash for_example.sh
```

This will output the values from 10 to 1 on a single line.
