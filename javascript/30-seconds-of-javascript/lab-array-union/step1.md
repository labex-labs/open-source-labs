# Array Union

> To start practicing coding, open the Terminal/SSH and type `node`.

Returns every element that exists in any of the two arrays at least once.

- Create a `Set` with all values of `a` and `b` and convert it to an array.

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));
```

```js
union([1, 2, 3], [4, 3, 2]); // [1, 2, 3, 4]
```
