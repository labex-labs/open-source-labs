# Functions with Parameters

Now that we've created a basic function, let's make it more flexible by adding parameters. Parameters allow us to pass information into our functions.

Open the `functions.sh` file again:

```bash
nano ~/project/functions.sh
```

Replace the content with the following code:

```bash
#!/bin/bash

# Function with a parameter
greet() {
  echo "Hello, $1!"
}

# Function with multiple parameters
calculate() {
  echo "The sum of $1 and $2 is $(($1 + $2))"
}

# Call functions with arguments
greet "Alice"
calculate 5 3
```

Let's examine this code:

- In the `greet` function, `$1` refers to the first argument passed to the function.
- In the `calculate` function, `$1` and `$2` refer to the first and second arguments, respectively.
- `$(($1 + $2))` performs arithmetic addition of the two parameters.

Save the file (Ctrl+X, Y, Enter) and run it:

```bash
./functions.sh
```

You should see:

```
Hello, Alice!
The sum of 5 and 3 is 8
```

If you don't see this output, make sure you've saved the changes to the file correctly.
