# Display the total cost

To see the result of our calculation, we need to print the total cost. Add the following line to your `fruit_basket.sh` file:

```bash
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))

# Display the total cost
echo "Total Cost is $TOTAL cents"
```

Let's break down this new line:

- `echo` is a command that prints text to the terminal.
- The text in quotes will be printed as-is, except for the `$TOTAL` part.
- When a variable name is preceded by `$` inside a string, Bash replaces it with the variable's value. This is called variable expansion.
- So if `TOTAL` is 128, the output will be "Total Cost is 128 cents".
