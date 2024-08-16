# Print the arrays and variables

Finally, let's add some code to print out our arrays and variables to see the results of our operations.

Add the following code to the end of your `arrays.sh` file:

```bash
# Print the arrays and variables
echo "NUMBERS array: ${NUMBERS[@]}"
echo "STRINGS array: ${STRINGS[@]}"
echo "The number of names listed in the NAMES array: $NumberOfNames"
echo "The second name on the NAMES list is: $second_name"
```

This code does the following:

- We use `echo` to print strings to the console.
- `${NUMBERS[@]}` and `${STRINGS[@]}` print all elements of these arrays.
- We print the `NumberOfNames` and `second_name` variables we created earlier.
