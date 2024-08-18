# Understanding Variable Scope

In shell scripts, variables are global by default. This means they can be accessed from anywhere in the script. However, you can use the `local` keyword to create variables that are only accessible within a function. This is called local scope.

Let's modify our `functions.sh` file to demonstrate this concept:

```bash
nano ~/project/functions.sh
```

Update the content with the following code:

```bash
#!/bin/bash

# Global variable
GLOBAL_VAR="I'm global"

# Function with a local variable
demonstrate_scope() {
  local LOCAL_VAR="I'm local"
  echo "Inside function: GLOBAL_VAR = $GLOBAL_VAR"
  echo "Inside function: LOCAL_VAR = $LOCAL_VAR"
}

# Call the function
demonstrate_scope

echo "Outside function: GLOBAL_VAR = $GLOBAL_VAR"
echo "Outside function: LOCAL_VAR = $LOCAL_VAR"
```

Here's what's happening in this script:

- We define a global variable `GLOBAL_VAR`.
- Inside the `demonstrate_scope` function, we define a local variable `LOCAL_VAR` using the `local` keyword.
- We print both variables inside the function.
- After calling the function, we try to print both variables again outside the function.

Save the file and run it:

```bash
./functions.sh
```

You should see output similar to this:

```
Inside function: GLOBAL_VAR = I'm global
Inside function: LOCAL_VAR = I'm local
Outside function: GLOBAL_VAR = I'm global
Outside function: LOCAL_VAR =
```

Notice that `LOCAL_VAR` is empty when accessed outside the function. This is because local variables are only accessible within the function where they are defined.
