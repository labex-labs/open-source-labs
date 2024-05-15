# The `for` Loop

The `for` loop is used to iterate over a list of values or the output of a command. Here is the basic syntax:

```bash
for item in [list]
do
    command(s)...
done
```

Create a file called `~/project/for.sh`.

To loop through an array, you can use the following example:

```bash
NAMES=("Joe" "Jenny" "Sara" "Tony")
for name in "${NAMES[@]}"; do
  echo "My name is $name"
done
```

```bash
cd ~/project
chmod +x for.sh
./for.sh
```

```text
My name is Joe
My name is Jenny
My name is Sara
My name is Tony
```

To loop through the output of a command, you can use the following example:

```bash
# create some txt files
touch file1.txt file2.txt file3.txt

# loop through the output of ls
for file in $(ls *.txt); do
  echo "File is: $file"
done
```

```text
File is: file1.txt
File is: file2.txt
File is: file3.txt
```
