# Define variables for fruit costs

Now that we have our script file, let's define some variables to store the costs of different fruits and the basket.

Add the following lines to your `fruit_basket.sh` file:

```bash
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1
```

Let's break this down:

- In Bash, we don't need to declare variables before using them. We simply assign a value to a variable name.
- Variable names are case-sensitive. By convention, we often use uppercase for constants (values that won't change).
- There should be no spaces around the `=` sign when assigning values.
- These values represent the cost in cents. For example, `COST_PINEAPPLE=50` means a pineapple costs 50 cents.
- We don't need to specify a data type. Bash treats these as strings by default, but will handle them as numbers when we perform arithmetic operations.
