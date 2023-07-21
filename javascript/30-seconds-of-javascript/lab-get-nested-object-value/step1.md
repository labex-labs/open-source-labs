# How to Retrieve Nested Object Properties from Path Strings

To practice coding, open the Terminal/SSH and type `node`.

The following function retrieves a set of properties from an object by using selectors specified in a path string. To achieve this, follow these steps:

1. Use `Array.prototype.map()` to iterate through each selector, and apply `String.prototype.replace()` to replace square brackets with dots.
2. Use `String.prototype.split()` to split each selector into an array of strings.
3. Use `Array.prototype.filter()` to remove any empty values.
4. Use `Array.prototype.reduce()` to retrieve the value indicated by each selector.

Here is the function:

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

You can use this function to retrieve values from a nested object using a path string. Here is an example:

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }],
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
