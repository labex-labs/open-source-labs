# Implement the first comparison loop

Let's implement the first comparison loop to find common elements between arrays `a` and `b`.

Add the following code to your script:

```bash
# Initialize an array to store common elements between a and b
z=()

# Compare arrays a and b
for x in "${a[@]}"; do
  for y in "${b[@]}"; do
    if [ $x = $y ]; then
      z+=($x)
    fi
  done
done

echo "Common elements between a and b: ${z[@]}"
```

Let's explain this code in detail:

- `z=()` initializes an empty array `z` to store the common elements.
- `for x in "${a[@]}"` is a loop that iterates over each element in array `a`. The `"${a[@]}"` syntax expands to all elements of the array.
- We then have a nested loop `for y in "${b[@]}"` that iterates over each element in array `b`.
- `if [ $x = $y ]` checks if the current element from `a` is equal to the current element from `b`.
- If they are equal, we add this element to array `z` using `z+=($x)`.
- Finally, we print the common elements using `echo "Common elements between a and b: ${z[@]}"`. The `${z[@]}` syntax expands to all elements of array `z`.
