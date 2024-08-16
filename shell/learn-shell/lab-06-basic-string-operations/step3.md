# Finding Character Position

Next, we'll learn how to find the position of a character in a string.

1. Add the following code to your `string_operations.sh` file:

   ```bash
   echo -e "\nStep 3: Finding Character Position"
   
   STRING="abcdefghijklmnopqrstuvwxyz"
   CHAR="j"
   
   POSITION=$(expr index "$STRING" "$CHAR")
   
   echo "The string is: $STRING"
   echo "We're looking for the character: $CHAR"
   echo "It is at position: $POSITION"
   ```

   Here's what this code does:

   - We define a `STRING` variable containing the alphabet.
   - We define a `CHAR` variable with the character we're looking for.
   - `expr index "$STRING" "$CHAR"` is a command that finds the position of `$CHAR` in `$STRING`.
   - We capture the output of this command in the `POSITION` variable using `$()`.
   - Finally, we print out the results.

2. Save the file and run the script again:

   ```bash
   ./string_operations.sh
   ```

You should see additional output similar to:

```
Step 3: Finding Character Position
The string is: abcdefghijklmnopqrstuvwxyz
We're looking for the character: j
It is at position: 10
```

Note that the position is 1-indexed, meaning the first character is at position 1, not 0.
