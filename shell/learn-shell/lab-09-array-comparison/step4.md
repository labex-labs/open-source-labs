# Implement the second comparison loop

Now, let's implement the second comparison loop to find common elements between array `c` and the previously found common elements in array `z`.

Add the following code to your script:

```bash
# Initialize an array to store common elements among a, b, and c
j=()

# Compare array c with the common elements found in z
for i in "${c[@]}"; do
  for k in "${z[@]}"; do
    if [ $i = $k ]; then
      j+=($i)
    fi
  done
done

echo "Common elements among a, b, and c: ${j[@]}"
```

This code is similar to the previous loop, but with a few key differences:

- We initialize a new empty array `j` to store the final common elements.
- The outer loop `for i in "${c[@]}"` iterates over elements in array `c`.
- The inner loop `for k in "${z[@]}"` iterates over the common elements we found between `a` and `b`, which are stored in array `z`.
- We compare elements from `c` with elements in `z`, and if there's a match, we add it to array `j`.
- Finally, we print the common elements among all three arrays.
