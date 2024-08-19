# The `until` Loop

The `until` loop is similar to the `while` loop, but with an important difference: it continues executing until a specified condition becomes true. It's like saying, "Keep doing this until this condition is true."

Create a new file called `until_loop.sh`:

```bash
touch until_loop.sh
```

Open the `until_loop.sh` file in the WebIDE and add the following content:

```bash
#!/bin/bash

# Count up to 5 using an until loop
count=1
echo "Counting up to 5:"
until [ $count -gt 5 ]; do
  echo $count
  count=$((count + 1))
  sleep 1 # Wait for 1 second
done
```

Let's break down this script:

1. We start with `count=1` as our initial value.
2. The condition `[ $count -gt 5 ]` means "until count is greater than 5".
3. Inside the loop, we print the current count, increase it by 1, and wait for a second.
4. This continues until count becomes greater than 5, at which point the loop ends.

Save the file and make it executable:

```bash
chmod +x until_loop.sh
```

Now, run the script:

```bash
./until_loop.sh
```

You'll see the numbers 1 through 5 printed, with a one-second pause between each:

```
Counting up to 5:
1
2
3
4
5
```

This demonstrates how an `until` loop can repeat an action until a condition becomes true.
