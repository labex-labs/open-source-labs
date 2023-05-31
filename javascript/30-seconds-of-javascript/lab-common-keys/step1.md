# Tips for Coding and Finding Common Keys

To practice coding, open the Terminal/SSH and type `node`.

To find the common keys between two objects, follow these steps:

1. Use `Object.keys()` to get the keys of the first object.
2. Use `Object.prototype.hasOwnProperty()` to check if the second object has a key that's in the first object.
3. Use `Array.prototype.filter()` to filter out keys that aren't in both objects.

Here's an example of the code:

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

You can test the code with this example:

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
