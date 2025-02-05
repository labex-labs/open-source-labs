# How to Get Function Property Names from an Object in JavaScript

To get an array of function property names from an object, use the `functions` function provided below. This function can also optionally include inherited properties.

Here's how to use the `functions` function:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` to iterate over the object's own properties.
3. If you want to include inherited properties, set the `inherited` argument to `true` and use `Object.getPrototypeOf()` to get the object's inherited properties.
4. Use `Array.prototype.filter()` to keep only those properties that are functions.
5. Omit the second argument, `inherited`, to not include inherited properties by default.

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

Here's an example usage of the `functions` function:

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
