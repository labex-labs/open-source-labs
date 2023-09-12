# Define the script and access the arguments

Create a new file and save it with `~/project/arguments.sh`.

Inside the script, you can access the passed arguments using special variables. The $1 variable references the first argument, $2 references the second argument, and so on. The $0 variable holds the name of the script itself.

```shell
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
```
