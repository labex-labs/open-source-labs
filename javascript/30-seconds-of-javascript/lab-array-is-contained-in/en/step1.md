# Function to Check if an Array is Contained in Another Array

To begin coding, open the Terminal/SSH and type `node`. This function checks whether all the elements of the first array are present in the second array, irrespective of their order.

Here are the steps to follow:

1. Use a `for...of` loop to iterate over a `Set` created from the first array.
2. Apply `Array.prototype.some()` to verify if all distinct values are present in the second array.
3. Use `Array.prototype.filter()` to compare the number of occurrences of each distinct value in both arrays.
4. If the count of any element is greater in the first array than the second one, return `false`. If not, return `true`.

Check out the code below to see how it works:

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

To test the function, use the following code:

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
