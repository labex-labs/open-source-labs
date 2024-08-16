# String Length

Now, let's learn how to determine the length of a string.

1. Add the following code to your `string_operations.sh` file:

   ```bash
   echo "Step 2: String Length"
   
   STRING="Hello, World!"
   LENGTH=${#STRING}
   
   echo "The string is: $STRING"
   echo "Its length is: $LENGTH"
   ```

   Let's break this down:

   - We define a variable `STRING` and assign it the value "Hello, World!".
   - `${#STRING}` is a special syntax that calculates the length of the string stored in the `STRING` variable.
   - We store this length in the `LENGTH` variable.
   - Finally, we print out both the string and its length.

2. Save the file. In most editors, you can do this by pressing Ctrl+S (or Cmd+S on Mac).

3. Make the script executable:

   ```bash
   chmod +x string_operations.sh
   ```

   This command changes the permissions of the file to make it executable. `chmod` stands for "change mode", and `+x` means "add execute permission".

4. Run the script:

   ```bash
   ./string_operations.sh
   ```

   The `./` tells the shell to look for the script in the current directory.

You should see output similar to:

```
Step 2: String Length
The string is: Hello, World!
Its length is: 13
```

If you don't see this output, double-check that you've saved the file and made it executable.
