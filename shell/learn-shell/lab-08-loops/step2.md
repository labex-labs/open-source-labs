# The `for` Loop

The `for` loop is used to iterate over a list of values. It's like saying, "For each item in this list, do something." Let's create a script that demonstrates how to use a `for` loop.

Create a new file called `for_loop.sh` in the `bash_loops` directory:

```bash
touch for_loop.sh
```

Now, open the `for_loop.sh` file in the WebIDE and add the following content:

```bash
#!/bin/bash

# Loop through an array of names
echo "Looping through an array:"
NAMES=("Alice" "Bob" "Charlie" "David")
for name in "${NAMES[@]}"; do
  echo "Hello, $name!"
done

echo # Print an empty line for readability

# Loop through a range of numbers
echo "Looping through a range of numbers:"
for i in {1..5}; do
  echo "Number: $i"
done
```

Let's break down what this script does:

1. The first loop goes through an array of names. For each name in the array, it prints a greeting.
2. The second loop uses a range `{1..5}` to count from 1 to 5.

The `"${NAMES[@]}"` syntax might look strange. The `@` means "all elements of the array," and the quotes and curly braces ensure that each element is treated as a separate item, even if it contains spaces.

Save the file and make it executable with this command:

```bash
chmod +x for_loop.sh
```

The `chmod +x` command makes the file executable, which means you can run it as a program.

Now, run the script:

```bash
./for_loop.sh
```

You should see output like this:

```
Looping through an array:
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, David!

Looping through a range of numbers:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

This demonstrates how `for` loops can iterate over both arrays and ranges of numbers.
