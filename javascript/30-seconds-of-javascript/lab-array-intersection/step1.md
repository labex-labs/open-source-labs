# Finding Array Intersection

To find the common elements between two arrays and remove duplicates, use the following code:

```js
const intersection = (arr1, arr2) => {
  const set = new Set(arr2);
  return [...new Set(arr1)].filter((elem) => set.has(elem));
};
```

To use this code, open the Terminal/SSH and type `node`. Then call the `intersection` function with two arrays as arguments, like this:

```js
intersection([1, 2, 3], [4, 3, 2]); // [2, 3]
```

This will return an array containing the elements that exist in both arrays, with duplicates removed.
