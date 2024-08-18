# Return Values from Functions

In shell scripting, functions don't return values in the same way as in other programming languages. Instead, they can either echo a result that can be captured, or they can modify a global variable. Let's explore both methods.

Open `functions.sh` again:

```bash
nano ~/project/functions.sh
```

Update the content with the following code:

```bash
#!/bin/bash

# Function that echoes a result
get_square() {
  echo $(($1 * $1))
}

# Function that modifies a global variable
RESULT=0
set_global_result() {
  RESULT=$(($1 * $1))
}

# Capture the echoed result
square_of_5=$(get_square 5)
echo "The square of 5 is $square_of_5"

# Use the function to modify the global variable
set_global_result 6
echo "The square of 6 is $RESULT"
```

Let's break this down:

- `get_square` function uses `echo` to output the result, which we capture using `$()` syntax.
- `set_global_result` function modifies the global variable `RESULT`.
- We use `$()` to capture the output of `get_square` into a variable.
- We call `set_global_result`, which modifies `RESULT`, and then we print `RESULT`.

Save the file and run it:

```bash
./functions.sh
```

You should see:

```
The square of 5 is 25
The square of 6 is 36
```

If you don't see this output, double-check your `functions.sh` file for any typos.
