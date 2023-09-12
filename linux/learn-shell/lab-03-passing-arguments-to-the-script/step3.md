# Handle multiple arguments

You can handle multiple arguments by accessing the variables $1, $2, $3, and so on, depending on the number of arguments passed.

```shell
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"
```

```text
$ ./arguments.sh argument1 argument2 argument3
Script name: ./arguments.sh
First argument: argument1
Second argument: argument2
Third argument: argument3
```
