# Revised Argument Coalescing Factory Code

To begin coding, open Terminal/SSH and type `node`. This function returns the first argument that evaluates to `true` based on the validator passed as an argument.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Use `Array.prototype.find()` to return the first argument that returns `true` from the provided argument validation function, `valid`. For instance,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Here, the `coalesceFactory` function is customized to create the `customCoalesce` function. The `customCoalesce` function filters out `null`, `undefined`, `NaN`, and empty strings from the provided arguments and returns the first argument that is not filtered out. The output of `customCoalesce(undefined, null, NaN, '', 'Waldo')` is `'Waldo'`.
