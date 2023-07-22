# Determining if Value is an Object

To determine if a passed value is an object, open the Terminal/SSH and type `node`. The following steps are taken:

- The `Object` constructor creates an object wrapper for the given value.
- If the value is `null` or `undefined`, an empty object is created and returned.
- If the value is not `null` or `undefined`, an object of a type corresponding to the given value is returned.

Here is an example function that checks if a value is an object:

```js
const isObject = (obj) => obj === Object(obj);
```

Here are some examples of using the `isObject` function:

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
