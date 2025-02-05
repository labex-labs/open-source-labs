# Function to Combine Arrays with a Provided Mapping Function

To begin coding, open the Terminal/SSH and type `node`.

This function returns an array of elements that exist in either of the two input arrays, after applying the provided mapping function to each element in both arrays.

Here are the steps to achieve this:

1. Create a new `Set` by applying the mapping function to all values in the first input array `a`.
2. Create another `Set` consisting of all the elements in `b` that do not match any values in the previously created `Set` when the mapping function is applied.
3. Combine the two sets and convert them to an array.
4. Return the resulting array.

Here is the code for the `unionBy` function:

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

Here are some examples of how to use the `unionBy` function:

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Output: [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Output: [{ id: 1 }, { id: 2 }, { id: 3 }]
```
