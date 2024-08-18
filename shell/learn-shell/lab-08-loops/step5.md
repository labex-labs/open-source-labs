# Using `break` and `continue` Statements

The `break` and `continue` statements are used to control the flow of loops. `break` exits a loop early, while `continue` skips the rest of the current iteration and moves to the next one.

Create a new file called `break_continue.sh`:

```bash
touch break_continue.sh
```

Open the `break_continue.sh` file in the WebIDE and add the following content:

```bash
#!/bin/zsh

# Using break to exit a loop early
echo "Demonstration of break:"
for i in {1..10}; do
  if [ $i -eq 6 ]; then
    echo "Breaking the loop at $i"
    break
  fi
  echo $i
done

echo # Print an empty line for readability

# Using continue to skip iterations
echo "Demonstration of continue (printing odd numbers):"
for i in {1..10}; do
  if [ $((i % 2)) -eq 0 ]; then
    continue
  fi
  echo $i
done
```

Let's break down this script:

1. In the first loop, we use `break` to exit the loop when `i` equals 6.
2. In the second loop, we use `continue` to skip even numbers. The condition `$((i % 2)) -eq 0` checks if a number is even (divisible by 2 with no remainder).

The `%` operator calculates the remainder after division. So `i % 2` will be 0 for even numbers and 1 for odd numbers.

Save the file and make it executable:

```bash
chmod +x break_continue.sh
```

Now, run the script:

```bash
./break_continue.sh
```

You should see output like this:

```
Demonstration of break:
1
2
3
4
5
Breaking the loop at 6

Demonstration of continue (printing odd numbers):
1
3
5
7
9
```

This demonstrates how `break` can exit a loop early, and how `continue` can skip certain iterations based on a condition.
