# How to Get an Array Without the Last Element

To practice coding, open the Terminal/SSH and type `node`. Here's how you can return all the elements of an array except the last one:

- Use `Array.prototype.slice()` to return all the elements of the array except the last one.

```js
const initial = (arr) => arr.slice(0, -1);
```

Here's an example:

```js
initial([1, 2, 3]); // [1, 2]
```
