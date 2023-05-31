# Function to Get Type of Value

To get the type of a value, use the following function:

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- The function returns `'undefined'` or `'null'` if the value is `undefined` or `null`.
- Otherwise, it returns the name of the constructor by using `Object.prototype.constructor` and `Function.prototype.name`.

Example usage:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
