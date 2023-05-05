## Solution

Use the following code in the `if_with_OR.sh` file:

```bash
#!/bin/bash

echo "Enter any number"
read n

if [[ ($n -eq 15 || $n -eq 45) ]]; then
  echo "You won the game"
else
  echo "You lost the game"
fi
```

Save the file and run it with the following command:

```bash
bash if_with_OR.sh
```
