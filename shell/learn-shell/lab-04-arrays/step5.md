# Access a specific element in an array

Now, let's access a specific element in our `NAMES` array. We'll get the second name.

Add this code to your `arrays.sh` file:

```bash
# Access the second name in the NAMES array
second_name=${NAMES[1]}
```

Here's what this code does:

- We're accessing the second element of the `NAMES` array with `${NAMES[1]}`.
- Remember, array indices in Bash start at 0, so `[1]` gives us the second element.
- We store this value in a variable called `second_name`.
