# JavaScript Function to Check if Object Has Key

To check if a target value exists in a JavaScript object, use the `hasKey` function.

The function takes two arguments: `obj`, the JSON object to search in, and `keys`, an array of keys to check for. Here are the steps to check if the object has the given key(s):

1. Check if the `keys` array is non-empty. If it is empty, return `false`.
2. Use the `Array.prototype.every()` method to iterate over the `keys` array and sequentially check each key to internal depth of the `obj`.
3. Use the `Object.prototype.hasOwnProperty()` method to check if `obj` does not have the current key or is not an object. If either of these conditions is true, stop propagation and return `false`.
4. Otherwise, assign the key's value to `obj` to use on the next iteration.
5. If the `keys` array has been iterated over successfully, return `true`.

Here's the code for the `hasKey` function:

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

Here are some examples of how to use the `hasKey` function:

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
