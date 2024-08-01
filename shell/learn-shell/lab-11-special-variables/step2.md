# Using the Special Variables

Let's see how to use these special variables with some examples:

```shell
#!/bin/bash
echo "Script Name: $0"

function func {
  for var in $*; do
    let i=i+1
    echo "The \$${i} argument is: ${var}"
  done
  echo "Total count of arguments: $#"
}

func We are argument
```

In the above example, we define a function called `func` that takes multiple arguments. We use the special variables `$*` and `$#` to iterate over the arguments and determine their count.

Create a file called `~/project/special.sh`.

```shell
cd ~/project
chmod +x special.sh
./special.sh
```

```text
Script Name: ./special.sh
The $1 argument is: We
The $2 argument is: are
The $3 argument is: argument
Total count of arguments: 3
```
