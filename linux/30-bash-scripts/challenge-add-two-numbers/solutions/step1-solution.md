## Solution

The following code can be used to create the `add_numbers.sh` script.

```bash
#!/bin/bash
echo "Enter first number"
read x
echo "Enter second number"
read y
((sum = x + y))
echo "The result of addition=$sum"
```

To run the script, execute the following command in the terminal:

```bash
bash add_numbers.sh
```
