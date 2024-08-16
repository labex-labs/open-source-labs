# Determine the number of elements in an array

One common operation with arrays is finding out how many elements they contain. Let's do this for our `NAMES` array.

Add the following code to your `arrays.sh` file:

```bash
# Get the number of elements in the NAMES array
NumberOfNames=${#NAMES[@]}
```

This line does the following:

- `${#NAMES[@]}` gives us the number of elements in the `NAMES` array.
- We store this value in a variable called `NumberOfNames`.
- The `@` symbol inside the brackets refers to all elements of the array.
- The `#` symbol before `NAMES` tells the shell to count the elements.
