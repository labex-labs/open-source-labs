# Use the $@ variable

The $@ variable holds a space-delimited string of all the arguments passed to the script. You can use it to loop through all the arguments and perform actions on each one.

```shell
#!/bin/bash
for arg in $@; do
  echo "Argument: $arg"
done
```

```text
$ ./arguments.sh argument1 argument2 argument3
Argument: argument1
Argument: argument2
Argument: argument3
```
