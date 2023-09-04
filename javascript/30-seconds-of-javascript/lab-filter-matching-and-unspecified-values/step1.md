# Filtering Objects by Condition and Keys

To filter an array of objects based on a condition, while also filtering out unspecified keys, use the `reducedFilter()` function.

Here are the steps to follow:

1. Use `Array.prototype.filter()` to filter the array based on the predicate `fn` so that it returns the objects for which the condition returned a truthy value.

2. Use `Array.prototype.map()` on the filtered array to return the new object.

3. Use `Array.prototype.reduce()` to filter out the keys which were not supplied as the `keys` argument.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {}),
  );
```

Here is an example usage of the `reducedFilter()` function:

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24,
  },
  {
    id: 2,
    name: "mike",
    age: 50,
  },
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Output: [{ id: 2, name: 'mike'}]
```

To start practicing coding, open the Terminal/SSH and type `node`.
