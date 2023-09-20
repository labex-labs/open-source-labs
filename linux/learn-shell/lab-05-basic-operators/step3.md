# Display the total cost

Finally, let's display the total cost of the fruit basket.

```bash
#!/bin/bash

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate the total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))

# Display the total cost
echo "Total Cost is $TOTAL"
```

```bash
cd ~/project
chmod +x operators.sh
./operators.sh
```

```text
Total Cost is 128
```
