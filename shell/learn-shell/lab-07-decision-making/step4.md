# Numeric Comparisons

You can use numeric comparisons to evaluate conditions in shell scripts. Here are some examples of numeric comparisons:

- `-lt`: less than
- `-gt`: greater than
- `-le`: less than or equal to
- `-ge`: greater than or equal to
- `-eq`: equal to
- `-ne`: not equal to

Update the `if.sh` script to include a numeric comparison that checks if the `NUMBER` variable is equal to the `APPLES` variable:

```bash
#!/bin/bash
NUMBER=10
APPLES=10
KING=GEORGE

if [ $NUMBER -gt 15 ]; then
  echo 1
fi
if [ $NUMBER -eq $APPLES ]; then
  echo 2
fi
```

The above script will print "2" because the expression is true.
