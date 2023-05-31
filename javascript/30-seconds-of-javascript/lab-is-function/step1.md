# Value Is Function

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if the given argument is a function.

- Use `typeof` to check if a value is classified as a function primitive.

```js
const isFunction = val => typeof val === 'function';
```

```js
isFunction('x'); // false
isFunction(x => x); // true
```
