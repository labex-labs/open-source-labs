# The `break` and `continue` Statements

The `break` and `continue` statements can be used to control the execution of a loop. `break` is used to exit the loop completely, while `continue` skips the rest of the current iteration and moves to the next one.

Here is an example that prints numbers from 0 to 4:

```bash
count=0
while [ $count -ge 0 ]; do
    echo "Value of count is: $count"
    count=$((count + 1))
    if [ $count -ge 5 ]; then
        break
    fi
done
```

Here is an example that prints only odd numbers from 1 to 10:

```bash
count=0
while [ $count -lt 10 ]; do
    count=$((count + 1))
    if [ $(($count % 2)) = 0 ]; then
        continue
    fi
    echo $count
done
```

Revise the file `~/project/while.sh` to use the `break` and `continue` statements.

```text
Value of count is: 1
Value of count is: 3
Value of count is: 5
Value of count is: 7
Value of count is: 9
```
