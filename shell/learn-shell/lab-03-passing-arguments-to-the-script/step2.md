# Access script arguments

Now, let's modify our script to access and display the arguments passed to it. In Shell scripting, special variables are used to access command-line arguments:

- `$0` represents the name of the script itself
- `$1`, `$2`, `$3`, etc., represent the first, second, third arguments, and so on

Add the following code to your `arguments.sh` file:

```bash
#!/bin/bash

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"
```

This script will display the script name and the first three arguments passed to it.

For beginners:

- The `$` symbol is used to reference variables in bash.
- `$0`, `$1`, `$2`, etc., are special variables that bash automatically sets for you when you run a script with arguments.
- If you run the script without any arguments, `$1`, `$2`, and `$3` will be empty, but the script will still run without errors.
