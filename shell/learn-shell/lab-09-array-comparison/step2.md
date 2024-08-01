# Compare arrays `a` and `b`

Next, compare the elements of arrays `a` and `b` to find the common elements. To do this, you can use nested loops.

```bash
# initialize an empty array to store the common elements
z=()

# loop through all elements of array a
for x in "${a[@]}"; do
  # set a flag to false
  in=false

  # loop through all elements of array b
  for y in "${b[@]}"; do
    if [ $x = $y ]; then
      # if a match is found, add the element to array z
      z+=($x)
    fi
  done
done
```
