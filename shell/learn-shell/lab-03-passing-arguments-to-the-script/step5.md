# Handle the number of arguments

Let's modify our script to handle different numbers of arguments. We'll use the `$#` special variable, which holds the number of arguments passed to the script.

Update your `arguments.sh` file with the following content:

```bash
#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No arguments provided."
elif [ $# -eq 1 ]; then
  echo "One argument provided: $1"
elif [ $# -eq 2 ]; then
  echo "Two arguments provided: $1 and $2"
else
  echo "More than two arguments provided:"
  echo "First argument: $1"
  echo "Second argument: $2"
  echo "Third argument: $3"
  echo "Total number of arguments: $#"
fi
```

This script uses conditional statements to handle different numbers of arguments.

For beginners:

- `$#` is a special variable that contains the number of arguments passed to the script.
- `[ $# -eq 0 ]` is a condition that checks if the number of arguments is equal to 0.
- `elif` is short for "else if". It allows you to check multiple conditions in sequence.
- The `-eq` operator means "equal to". There are other operators like `-lt` (less than), `-gt` (greater than), etc.
