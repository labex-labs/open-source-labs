# String Comparisons

You can also use string comparisons to evaluate conditions. Here are some examples of string comparisons:

- `"="`: equal to
- `"=="`: equal to
- `"!="`: not equal to
- `"-z"`: empty string

```bash
#!/bin/bash
NUMBER=10
APPLES=12
KING=GEORGE

if [[ ($APPLES -eq 12) || ("$KING" = "LUIS") ]] ; then
  echo 3
fi
```
