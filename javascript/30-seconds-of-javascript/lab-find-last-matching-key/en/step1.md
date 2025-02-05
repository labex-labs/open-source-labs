# Function to Find the Last Key that Matches a Condition

To find the last key in an object that satisfies a given condition, use the `findLastKey` function. This function takes an object and a testing function as arguments. If a matching key is found, the function returns it. Otherwise, it returns `undefined`. Here are the steps the function takes to find the last key:

1. Use `Object.keys()` to get all the properties of the object.
2. Use `Array.prototype.reverse()` to reverse the order of the keys.
3. Use `Array.prototype.find()` to test the provided function for each key-value pair. The callback function receives three arguments - the value, the key, and the object.
4. If a matching key is found, return it.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

Here's an example of using `findLastKey`:

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

To use this function, open the Terminal/SSH and type `node` to start practicing coding.
