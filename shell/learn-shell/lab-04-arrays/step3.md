# Add elements to the arrays

Now that we have our empty arrays, let's add some elements to them.

Add the following code to your `arrays.sh` file, below the array initializations:

```bash
# Add elements to NUMBERS array
NUMBERS+=(1)
NUMBERS+=(2)
NUMBERS+=(3)

# Add elements to STRINGS array
STRINGS+=("hello")
STRINGS+=("world")

# Add elements to NAMES array
NAMES+=("John")
NAMES+=("Eric")
NAMES+=("Jessica")
```

Here's what this code does:

- We use the `+=` operator to append elements to our arrays.
- For `NUMBERS`, we're adding the integers 1, 2, and 3.
- For `STRINGS`, we're adding the words "hello" and "world".
- For `NAMES`, we're adding three names: "John", "Eric", and "Jessica".
- Note that we enclose string elements in quotes, but numbers don't need quotes.
