# Instructions for Finding Mapped Array Intersection

To find common elements in two arrays after applying a function to each element of both arrays, follow these steps:

1. Open Terminal/SSH and type `node`.
2. Use the code provided below:

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. In the code, replace `a` and `b` with your arrays and `fn` with the function you want to apply to each element.
4. Run the code to get the resulting array with common elements.

Example:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

In the first example, the function `Math.floor` is applied to the arrays `[2.1, 1.2]` and `[2.3, 3.4]`, returning the common element `[2.1]`.
In the second example, the function `x => x.title` is applied to the arrays `[{ title: 'Apple' }, { title: 'Orange' }]` and `[{ title: 'Orange' }, { title: 'Melon' }]`, returning the common element `[{ title: 'Orange' }]`.
