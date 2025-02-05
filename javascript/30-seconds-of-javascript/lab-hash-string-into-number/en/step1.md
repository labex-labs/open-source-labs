# How to Hash a String into a Number Using JavaScript

To hash an input string into a whole number using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.split()` and `Array.prototype.reduce()` methods to create a hash of the input string, utilizing bit shifting.
3. Here's the code for the `sdbm` function that implements the hashing algorithm:

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. To test the function, call it with a string argument:

```js
sdbm("name"); // -3521204949
```

This will return the hash value for the input string "name".
