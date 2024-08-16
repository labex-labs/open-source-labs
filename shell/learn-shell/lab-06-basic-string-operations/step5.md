# String Replacement

Finally, let's learn how to replace parts of a string.

1. Add the following code to your `string_operations.sh` file:

   ```bash
   echo -e "\nStep 5: String Replacement"
   
   STRING="The quick brown fox jumps over the lazy dog"
   echo "Original string: $STRING"
   
   # Replace the first occurrence of 'o' with 'O'
   NEW_STRING=${STRING/o/O}
   echo "Replacing first 'o' with 'O': $NEW_STRING"
   
   # Replace all occurrences of 'o' with 'O'
   NEW_STRING=${STRING//o/O}
   echo "Replacing all 'o' with 'O': $NEW_STRING"
   
   # Replace 'quick' with 'slow' if it's at the beginning of the string
   NEW_STRING=${STRING/#quick/slow}
   echo "Replacing 'quick' with 'slow' at the beginning: $NEW_STRING"
   
   # Replace 'dog' with 'cat' if it's at the end of the string
   NEW_STRING=${STRING/%dog/cat}
   echo "Replacing 'dog' with 'cat' at the end: $NEW_STRING"
   ```

   This code demonstrates various string replacement techniques:

   - `${STRING/o/O}` replaces the first occurrence of 'o' with 'O'.
   - `${STRING//o/O}` replaces all occurrences of 'o' with 'O'.
   - `${STRING/#quick/slow}` replaces 'quick' with 'slow', but only if 'quick' is at the beginning of the string.
   - `${STRING/%dog/cat}` replaces 'dog' with 'cat', but only if 'dog' is at the end of the string.

2. Save the file and run the script one last time:

   ```bash
   ./string_operations.sh
   ```

You should see additional output similar to:

```
Step 5: String Replacement
Original string: The quick brown fox jumps over the lazy dog
Replacing first 'o' with 'O': The quick brOwn fox jumps over the lazy dog
Replacing all 'o' with 'O': The quick brOwn fOx jumps Over the lazy dOg
Replacing 'quick' with 'slow' at the beginning: The quick brown fox jumps over the lazy dog
Replacing 'dog' with 'cat' at the end: The quick brown fox jumps over the lazy cat
```

Notice how each replacement operation affects the string differently.
