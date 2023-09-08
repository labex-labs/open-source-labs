# How to Get a Nested Value in a JSON Object

To retrieve a target value from a nested JSON object based on a given key, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Check if the `target` exists in the `obj` using the `in` operator.
- If the `target` is found, return the corresponding value in the `obj`.
- If the `target` is not found, use `Object.values()` and `Array.prototype.reduce()` to recursively call the `dig` function on each nested object until the first matching key/value pair is found.

Here is the code for the `dig` function:

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

To use the `dig` function, first create a JSON object with nested levels, like this:

```js
const data = {
  level1: {
    level2: {
      level3: "some data"
    }
  }
};
```

Then, call the `dig` function with the JSON object and the desired key:

```js
dig(data, "level3"); // 'some data'
dig(data, "level4"); // undefined
```

These examples will return the value of the `level3` key in the `data` object and `undefined` for the non-existent `level4` key.
