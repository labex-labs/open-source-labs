# Array to Object Based on Key

> To start practicing coding, open the Terminal/SSH and type `node`.

Creates an object from an array, using the specified key and excluding it from each value.

- Use `Array.prototype.reduce()` to create an object from `arr`.
- Use object destructuring to get the value of the given `key` and the associated `data` and add the key-value pair to the object.

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

```js
indexOn([
  { id: 10, name: 'apple' },
  { id: 20, name: 'orange' }
], 'id');
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
