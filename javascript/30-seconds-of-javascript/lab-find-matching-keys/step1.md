# Find Matching Keys

To find all the keys in an object that match a given value, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` to get all the properties of the object.
3. Use `Array.prototype.filter()` to test each key-value pair and return all keys that are equal to the given value.

Here's an example function that implements this logic:

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

You can use this function like this:

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20,
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
