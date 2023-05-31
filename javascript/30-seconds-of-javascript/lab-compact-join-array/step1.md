# Here's a tip on how to Compact and Join an Array

To start practicing coding, open the Terminal/SSH and type `node`.

Here's how to remove falsy values from an array and combine the remaining values into a string:

- Use `Array.prototype.filter()` to filter out falsy values such as `false`, `null`, `0`, `""`, `undefined`, and `NaN`.
- Use `Array.prototype.join()` to join the remaining values into a string.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

Then call the function and pass an array as an argument:

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
