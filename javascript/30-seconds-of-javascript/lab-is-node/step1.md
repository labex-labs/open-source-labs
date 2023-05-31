# How to Determine if the Current Runtime Environment is Node.js

To determine if the current runtime environment is Node.js, follow these steps:

1. Open the Terminal/SSH.
2. Type `node`.
3. Use the `process` global object that provides information about the current Node.js process.
4. Check if `process`, `process.versions`, and `process.versions.node` are defined.

Here's the code to determine if the current runtime environment is Node.js:

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

You can test the code by calling the `isNode` function:

```js
isNode(); // true (Node)
isNode(); // false (browser)
```
