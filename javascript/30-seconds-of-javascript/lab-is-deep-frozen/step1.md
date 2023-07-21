# How to Check if an Object is Deeply Frozen

To check if an object is deeply frozen, use the following steps in JavaScript:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to check if all the properties of the object are deeply frozen.
3. Use `Object.isFrozen()` on the given object to check if it is shallowly frozen.
4. Use `Object.keys()` to get all the properties of the object and `Array.prototype.every()` to check that all keys are either deeply frozen objects or non-object values.

Here's an example code snippet to check if an object is deeply frozen:

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

You can use the `isDeepFrozen` function to check if an object is deeply frozen like this:

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
