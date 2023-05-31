# How to Map an Object to an Array in JavaScript

To map an object to an array in JavaScript, you can use the `listify()` function. Here's how you can do it:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `Object.entries()` to get an array of the object's key-value pairs.

3. Use `Array.prototype.reduce()` to map the array to an object.

4. Use `mapFn` to map the keys and values of the object and `Array.prototype.push()` to add the mapped values to the array.

Here's the code for the `listify()` function:

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

And here's an example of how to use it with an object called `people`:

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

With this function, you can easily map an object to an array in JavaScript.
