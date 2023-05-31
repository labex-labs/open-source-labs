# Symbolize Object Keys

> To start practicing coding, open the Terminal/SSH and type `node`.

Creates a new object, converting each key to a `Symbol`.

- Use `Object.keys()` to get the keys of `obj`.
- Use `Array.prototype.reduce()` and `Symbol` to create a new object where each key is converted to a `Symbol`.

```js
const symbolizeKeys = obj =>
  Object.keys(obj).reduce(
    (acc, key) => ({ ...acc, [Symbol(key)]: obj[key] }),
    {}
  );
```

```js
symbolizeKeys({ id: 10, name: 'apple' });
// { [Symbol(id)]: 10, [Symbol(name)]: 'apple' }
```
