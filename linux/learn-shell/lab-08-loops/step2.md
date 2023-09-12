# The `while` Loop

The `while` loop is used to execute a block of code as long as a certain condition is true. Here is the basic syntax:

```bash
while [ condition ]
do
    command(s)...
done
```

Here is an example that counts down from 4:

```bash
count=4
while [ $count -gt 0 ]; do
    echo "Value of count is: $count"
    count=$(($count - 1))
done
```

Create a file called `~/project/while.sh`.

```bash
cd ~/project
chmod +x while.sh
./while.sh
```

```text
Value of count is: 4
Value of count is: 3
Value of count is: 2
Value of count is: 1
```
