# String Comparisons

You can also use string comparisons to evaluate conditions. Here are some examples of string comparisons:

- `"="`: equal to
- `"=="`: equal to
- `"!="`: not equal to
- `"-z"`: empty string

Update the `if.sh` script to include a string comparison that checks if the `KING` variable is equal to "LUIS":

```bash
#!/bin/bash
NUMBER=10
APPLES=12
KING=LUIS

if [[ ($APPLES -eq 12) || ("$KING" = "LUIS") ]]; then
  echo 3
fi
```

The above script will print "3" because the expression is true.
