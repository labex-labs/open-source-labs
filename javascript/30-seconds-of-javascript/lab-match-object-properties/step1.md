# How to Compare Object Properties in JavaScript

To compare two objects and check if they have the same property values, use the `matches` function. Here's how to use it:

1. Open the Terminal/SSH and type `node` to start coding.
2. Copy and paste the `matches` function code into your JavaScript file.
3. Call the function and pass two objects as arguments. The first object is the one you want to compare, and the second object is the one you want to compare it to.

```js
matches({ age: 25, hair: "long", beard: true }, { hair: "long", beard: true });
// true
matches({ hair: "long", beard: true }, { age: 25, hair: "long", beard: true });
// false
```

The `matches` function uses `Object.keys()` to get all the keys of the second object and then checks if all keys exist in the first object and have the same values using `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` and strict comparison.
