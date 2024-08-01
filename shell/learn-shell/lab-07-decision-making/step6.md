# Logic Combinations

You can combine multiple conditions using logical operators like `&&` (logical AND) and `||` (logical OR).

Update the `if.sh` script to include a logical OR operator that checks if the sum of the `NUMBER` and `APPLES` variables is less than or equal to 32:

```bash
#!/bin/bash
NUMBER=10
APPLES=12
KING=GEORGE

if [[ $(($NUMBER + $APPLES)) -le 32 ]]; then
  echo 4
fi
```

The above script will print "4" because the expression is true.
