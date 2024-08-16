# Initialize empty arrays

Now that we have our script file, let's start by initializing three empty arrays.

Add the following code to your `arrays.sh` file:

```bash
#!/bin/bash

# Initialize empty arrays
NUMBERS=()
STRINGS=()
NAMES=()
```

Let's break down what this code does:

- The first line `#!/bin/bash` is called a shebang. It tells the system that this script should be executed by the Bash shell.
- We're creating three empty arrays: `NUMBERS`, `STRINGS`, and `NAMES`.
- The `()` syntax initializes an empty array.
