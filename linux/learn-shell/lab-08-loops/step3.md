# The `until` Loop

The `until` loop is the opposite of the `while` loop. It continues executing a block of code until a certain condition becomes true. Here is the basic syntax:

```bash
until [ condition ]
do
    command(s)...
done
```

Here is an example that counts up to 5:

```bash
count=1
until [ $count -gt 5 ]; do
    echo "Value of count is: $count"
    count=$(($count + 1))
done
```

Revise the file `~/project/while.sh` to use the `until` loop.

```text
Value of count is: 1
Value of count is: 2
Value of count is: 3
Value of count is: 4
Value of count is: 5
```
