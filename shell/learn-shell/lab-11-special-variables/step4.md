# Using Special Variables in Functions

Special variables can also be used within functions. Let's create a script to demonstrate this.

1. Create a new file named `function_vars.sh`:

```bash
touch ~/project/function_vars.sh
```

2. Open the file in the WebIDE editor and add the following content:

```bash
#!/bin/bash

function print_args {
  echo "Function Name: $0"
  echo "First Argument: $1"
  echo "Second Argument: $2"
  echo "All Arguments: $@"
  echo "Number of Arguments: $#"
}

echo "Calling function with two arguments:"
print_args hello world

echo "Calling function with four arguments:"
print_args one two three four
```

This script defines a function `print_args` that uses special variables. Then it calls this function twice with different numbers of arguments.

3. Save the file and make it executable:

```bash
chmod +x ~/project/function_vars.sh
```

4. Run the script:

```bash
./function_vars.sh
```

You should see output similar to this:

```
Calling function with two arguments:
Function Name: ./function_vars.sh
First Argument: hello
Second Argument: world
All Arguments: hello world
Number of Arguments: 2
Calling function with four arguments:
Function Name: ./function_vars.sh
First Argument: one
Second Argument: two
All Arguments: one two three four
Number of Arguments: 4
```

Notice that:

- `$0` still refers to the script name, not the function name.
- `$1`, `$2`, `$@`, and `$#` work for function arguments just like they do for script arguments.
- The values of these variables change each time the function is called with different arguments.
