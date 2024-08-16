# Substring Extraction

Now, let's learn how to extract a portion of a string.

1. Add the following code to your `string_operations.sh` file:

   ```bash
   echo -e "\nStep 4: Substring Extraction"
   
   STRING="The quick brown fox jumps over the lazy dog"
   START=10
   LENGTH=5
   
   SUBSTRING=${STRING:$START:$LENGTH}
   
   echo "The original string is: $STRING"
   echo "Extracting 5 characters starting from position 10:"
   echo "The substring is: $SUBSTRING"
   ```

   Let's break this down:

   - We define a `STRING` variable with a sample sentence.
   - `START` is the position where we want to start extracting (remember, it's 0-indexed here).
   - `LENGTH` is how many characters we want to extract.
   - `${STRING:$START:$LENGTH}` is the syntax for extracting a substring. It means "from `STRING`, take `LENGTH` characters starting at position `START`".
   - We store this substring in the `SUBSTRING` variable and then print everything out.

2. Save the file and run the script again:

   ```bash
   ./string_operations.sh
   ```

You should see additional output similar to:

```
Step 4: Substring Extraction
The original string is: The quick brown fox jumps over the lazy dog
Extracting 5 characters starting from position 10:
The substring is: brown
```

Note that unlike the `expr index` command, the string positions here start at 0, not 1. This is why we get "brown" starting from position 10.
