# JavaScript Function for Finding the Last Matching Value

To find the last element in an array that satisfies a given condition, use the following JavaScript function:

```js
const findLast = (arr, fn) => arr.filter(fn).pop();
```

To use this function, pass in the array you want to search and a function that returns a truthy value for the elements you want to match.

For example, `findLast([1, 2, 3, 4], n => n % 2 === 1);` will return `3`, as it finds the last odd number in the array.

To start practicing coding, open the Terminal/SSH and type `node`.
