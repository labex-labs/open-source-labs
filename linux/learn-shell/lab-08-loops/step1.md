# The `for` Loop

The `for` loop is used to iterate over a list of values or the output of a command. Here is the basic syntax:

```bash
for item in [list]
do
    command(s)...
done
```

To loop through an array, you can use the following example:

```bash
NAMES=("Joe" "Jenny" "Sara" "Tony")
for name in "${NAMES[@]}"; do
    echo "My name is $name"
done
```

To loop through the output of a command, you can use the following example:

```bash
for file in $(ls *.txt); do
    echo "File is: $file"
done
```
