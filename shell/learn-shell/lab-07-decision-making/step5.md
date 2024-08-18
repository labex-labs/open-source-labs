# String Comparisons and Logical Operators

Lastly, let's explore string comparisons and logical operators. Create a new file called `string_logic.sh`:

```bash
touch string_logic.sh
```

Open `string_logic.sh` in the WebIDE and add the following content:

```bash
#!/bin/bash

STRING1="hello"
STRING2="world"
NUMBER1=5
NUMBER2=10

if [ "$STRING1" = "hello" ] && [ "$STRING2" = "world" ]; then
  echo "Both strings match"
fi

if [ $NUMBER1 -lt 10 ] || [ $NUMBER2 -gt 5 ]; then
  echo "At least one of the number conditions is true"
fi

if [[ "$STRING1" != "$STRING2" ]]; then
  echo "The strings are different"
fi

if [[ -z "$STRING3" ]]; then
  echo "STRING3 is empty or not set"
fi
```

This script demonstrates several new concepts:

1. String equality comparison (`=`): This checks if two strings are exactly the same.

2. Logical AND (`&&`): This operator allows you to combine two conditions. Both conditions must be true for the overall expression to be true.

3. Logical OR (`||`): This operator also combines two conditions, but only one needs to be true for the overall expression to be true.

4. String inequality comparison (`!=`): This checks if two strings are different.

5. Checking if a string is empty (`-z`): This is true if the string is empty (has zero length).

Also, notice the use of double square brackets `[[ ]]` in some of the if statements. These are an enhanced version of the single square brackets and are preferred in Bash scripts when possible. They allow for more complex expressions and have fewer surprises with regard to word splitting and pathname expansion.

Make the script executable and run it:

```bash
chmod +x string_logic.sh
./string_logic.sh
```

You should see all four echo statements printed, because all the conditions in the script are true.

Try changing some of the values (like setting `STRING1` to something other than "hello") and see how it affects the output.
