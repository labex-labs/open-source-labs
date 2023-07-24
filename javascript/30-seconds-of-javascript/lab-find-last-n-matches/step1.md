# Instructions to find Last N Matches

To find the last `n` elements that match a certain condition, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `findLastN` function provided below.
3. Provide an array `arr` and a `matcher` function that returns a truthy value for the elements you want to match.
4. Optionally, you can also provide the number `n` of matches you want to return (default is 1).
5. The function will execute the `matcher` function for each element of `arr` using a `for` loop, starting from the last element.
6. If an element matches the `matcher` condition, it will be added to the results array using `Array.prototype.unshift()`, which prepends elements to the array.
7. When the length of the results array is equal to `n`, the function will return the results.
8. If there are no matches or `n` is greater than the number of matches, an empty array will be returned.

```js
const findLastN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.unshift(el);
    if (res.length === n) return res;
  }
  return res;
};
```

Here are some examples of how to use the `findLastN` function:

```js
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [4, 6]
findLastN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
