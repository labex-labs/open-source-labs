# How to Find the Min and Max of an Array Using a Provided Function

To practice coding, open the Terminal or SSH and type `node`.

Here's a function that returns the minimum and maximum values of an array, based on a provided function that sets the comparison rule:

```js
const reduceWhich = (arr, comparator = (a, b) => a - b) =>
  arr.reduce((a, b) => (comparator(a, b) >= 0 ? b : a));
```

To use it, follow these steps:

1. Call `reduceWhich` with the array you want to process and the optional `comparator` function.
2. The `reduceWhich` function will use `Array.prototype.reduce()` in combination with the `comparator` function to return the appropriate element in the array.
3. If you omit the second argument (`comparator`), the default function will be used, which returns the minimum element in the array.

Here are some examples of how to use `reduceWhich`:

```js
reduceWhich([1, 3, 2]); // 1
reduceWhich([1, 3, 2], (a, b) => b - a); // 3
reduceWhich(
  [
    { name: "Tom", age: 12 },
    { name: "Jack", age: 18 },
    { name: "Lucy", age: 9 },
  ],
  (a, b) => a.age - b.age,
); // {name: 'Lucy', age: 9}
```

In the examples above, the first call to `reduceWhich` returns the minimum value of the array `[1, 3, 2]`, which is `1`. The second call returns the maximum value of the same array, based on the `comparator` function that reverses the order of comparison. The third call returns the object in the array that has the minimum `age` property, based on the `comparator` function that compares the `age` properties of the objects.
