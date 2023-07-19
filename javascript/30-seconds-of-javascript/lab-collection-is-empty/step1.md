# Checking if a Collection is Empty

To check if a collection is empty, you can open the Terminal/SSH and type `node`. This program checks if a value is an empty object/collection, has no enumerable properties, or is any type that is not considered a collection.

To use the program, check if the provided value is `null` or if its `length` is equal to `0`. Here's an example code:

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

You can then test the program using the following codes:

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - type is not considered a collection
isEmpty(true); // true - type is not considered a collection
```
