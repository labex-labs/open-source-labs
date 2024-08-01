# Calculate the total cost

Next, we will calculate the total cost of a fruit basket, which contains 1 pineapple, 2 bananas, and 3 watermelons.

```bash
#!/bin/bash

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate the total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))
```
