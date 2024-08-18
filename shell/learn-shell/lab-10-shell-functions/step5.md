# Advanced Function - ENGLISH_CALC

Now that we've covered the basics of shell functions, let's create a more advanced function called `ENGLISH_CALC`. This function will take three arguments: two numbers and an operation (plus, minus, or times).

Open the `functions.sh` file:

```bash
nano ~/project/functions.sh
```

Replace the content with the following code:

```bash
#!/bin/bash

ENGLISH_CALC() {
  local num1=$1
  local operation=$2
  local num2=$3
  local result

  case $operation in
    plus)
      result=$((num1 + num2))
      echo "$num1 + $num2 = $result"
      ;;
    minus)
      result=$((num1 - num2))
      echo "$num1 - $num2 = $result"
      ;;
    times)
      result=$((num1 * num2))
      echo "$num1 * $num2 = $result"
      ;;
    *)
      echo "Invalid operation. Please use 'plus', 'minus', or 'times'."
      return 1
      ;;
  esac
}

# Test the function
ENGLISH_CALC 3 plus 5
ENGLISH_CALC 5 minus 1
ENGLISH_CALC 4 times 6
ENGLISH_CALC 2 divide 2 # This should show an error message
```

Let's break down this function:

- We use `local` variables to store our inputs and results. This is good practice to avoid interfering with any global variables.
- We use a `case` statement to handle different operations. This is similar to a switch statement in other languages.
- For each valid operation, we perform the calculation and echo the result.
- If an invalid operation is provided, we echo an error message and return 1 (in shell scripts, a non-zero return value indicates an error).
- At the end, we test our function with various inputs, including an invalid operation.

Save the file and run it:

```bash
./functions.sh
```

You should see the following output:

```
3 + 5 = 8
5 - 1 = 4
4 * 6 = 24
Invalid operation. Please use 'plus', 'minus', or 'times'.
```

If you don't see this output, double-check your `functions.sh` file for any typos.
