# Loop through all arguments

Finally, let's modify our script to loop through all provided arguments using the `$@` special variable, which represents all command-line arguments.

Update your `arguments.sh` file with the following content:

```bash
#!/bin/bash

echo "Total number of arguments: $#"
echo "All arguments:"

count=1
for arg in "$@"; do
  echo "Argument $count: $arg"
  count=$((count + 1))
done
```

This script uses a `for` loop to iterate through all arguments and display them with their position.

For beginners:

- `$@` is a special variable that contains all the arguments passed to the script.
- The `for` loop is used to iterate over a list of items. In this case, it's iterating over all the arguments.
- `$((count + 1))` is arithmetic expansion in bash. It's used to increment the count variable.
- This script will work with any number of arguments, making it more flexible than our previous versions.
