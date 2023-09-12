# Call a Function

Functions can be called simply by writing their names. A function call is equivalent to a command. You can also pass parameters to functions by specifying them after the function name. The first parameter is referred to in the function as `$1`, the second as `$2`, and so on.

```bash
function function_B {
  echo "Function B."
}
function function_A {
  echo "$1"
}
function adder {
  echo "$(($1 + $2))"
}

# FUNCTION CALLS
# Pass parameter to function A
function_A "Function A."     # Function A.
function_B                   # Function B.
# Pass two parameters to function adder
adder 12 56                  # 68
```
