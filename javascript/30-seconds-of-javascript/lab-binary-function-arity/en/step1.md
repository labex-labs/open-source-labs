# Function that accepts up to two arguments

To begin coding, open the Terminal/SSH and enter `node`.

The `binary` function is created with the ability to accept up to two arguments while disregarding any additional ones.

The provided `fn` function is called with the first two arguments given.

Here is the code:

```js
const binary = (fn) => (a, b) => fn(a, b);
```

And here's an example usage:

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
