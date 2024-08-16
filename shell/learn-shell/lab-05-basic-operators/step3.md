# Calculate the total cost

Now that we have our costs defined, let's calculate the total cost of a fruit basket containing 1 pineapple, 2 bananas, and 3 watermelons.

Add the following line to your `fruit_basket.sh` file:

```bash
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))
```

Let's examine this new line:

- `$((  ))` is Bash's syntax for arithmetic operations. Anything inside these double parentheses is treated as an arithmetic expression.
- Inside the arithmetic expression, we don't need to use `$` before variable names.
- We're performing several operations:
  - `COST_PINEAPPLE`: The cost of 1 pineapple
  - `(COST_BANANA * 2)`: The cost of 2 bananas
  - `(COST_WATERMELON * 3)`: The cost of 3 watermelons
  - `COST_BASKET`: The cost of the basket itself
- These values are all added together, and the result is stored in the `TOTAL` variable.

Note: Bash only handles integer arithmetic. If we were dealing with dollars and cents, we'd need to use a tool like `bc` for floating-point arithmetic.
