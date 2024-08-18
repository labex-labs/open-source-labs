# The `while` Loop

The `while` loop executes a block of code as long as a specified condition is true. It's like saying, "While this condition is true, keep doing this."

Create a new file called `while_loop.sh`:

```bash
touch while_loop.sh
```

Open the `while_loop.sh` file in the WebIDE and add the following content:

```bash
#!/bin/zsh

# Simple countdown using a while loop
count=5
echo "Countdown:"
while [ $count -gt 0 ]; do
  echo $count
  count=$((count - 1))
  sleep 1 # Wait for 1 second
done
echo "Blast off!"
```

Let's break down this script:

1. We start with `count=5` to set our initial countdown value.
2. The condition `[ $count -gt 0 ]` means "while count is greater than 0".
3. Inside the loop, we print the current count, decrease it by 1, and wait for a second.
4. This continues until count reaches 0, at which point the loop ends.

The `sleep 1` command pauses the script for 1 second, creating a real-time countdown effect.

Save the file and make it executable:

```bash
chmod +x while_loop.sh
```

Now, run the script:

```bash
./while_loop.sh
```

You'll see a countdown from 5 to 1, with a one-second pause between each number:

```
Countdown:
5
4
3
2
1
Blast off!
```

This demonstrates how a `while` loop can repeat an action until a condition is no longer true.
