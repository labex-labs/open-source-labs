# How to Retrieve a Nested Value in an Object Using an Array of Keys

To retrieve a specific value from a nested JSON object, you can use the `deepGet` function. This function takes in an object and an array of keys, and returns the target value if it exists in the object.

To use the `deepGet` function:

- Create an array of the keys you want to retrieve from the nested JSON object.
- Call the `deepGet` function with the object and the array of keys.
- The function will return the target value if it exists, or `null` if it does not.

Here is the code for the `deepGet` function:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

And here is an example of how to use the `deepGet` function:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // returns 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // returns null
```

To start practicing coding, open the Terminal/SSH and type `node`.
