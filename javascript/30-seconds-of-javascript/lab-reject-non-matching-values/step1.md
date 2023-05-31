# Filtering Array Values

To filter an array based on a predicate function and return only values for which the predicate function returns false, follow these steps:

1. Use `Array.prototype.filter()` in combination with the predicate function, `pred`.
2. The filter method will return only the values for which the predicate function returns `false`.
3. To reject non-matching values, pass the predicate function and the array to the `reject()` function.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

Here are some examples of how to use the `reject()` function:

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

By following these steps, you can easily filter an array based on a predicate function and reject non-matching values.
