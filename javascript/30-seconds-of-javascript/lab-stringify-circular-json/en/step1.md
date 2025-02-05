# How to Stringify Circular JSON

To stringify a JSON object that contains circular references, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a `WeakSet` to store and check seen values using `WeakSet.prototype.add()` and `WeakSet.prototype.has()`.
3. Use `JSON.stringify()` with a custom replacer function that omits values already in `seen`, and adds new values if necessary.
4. ⚠️ **NOTICE:** This function finds and removes circular references, which causes circular data loss in the serialized JSON.

Here's the code for the `stringifyCircularJSON` function:

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

To test the function, you can create an object with a circular reference and call `stringifyCircularJSON`:

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
