# Compare array `c` with array `z`

Next, compare the elements of array `c` with the elements of array `z` to find the common elements. Again, you can use nested loops for this step.

```bash
# initialize an empty array to store the common elements
j=()

# loop through all elements of array c
for i in "${c[@]}"; do
  # set a flag to false
  in=false

  # loop through all elements of array z
  for k in "${z[@]}"; do
    if [ $i = $k ]; then
      # if a match is found, add the element to array j
      j+=($i)
    fi
  done
done
```
