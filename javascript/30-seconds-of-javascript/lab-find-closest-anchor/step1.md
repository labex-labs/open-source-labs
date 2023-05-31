# How to Find the Closest Anchor Node

To find the closest anchor node to a given node, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use a `for` loop and `Node.parentNode` to traverse the node tree upwards from the given `node`.
3. Check if any given node is an anchor (`'a'`) using `Node.nodeName` and `String.prototype.toLowerCase()`.
4. If a matching node is found, return it. If no matching node is found, return `null`.

Here's the code that accomplishes this:

```js
const findClosestAnchor = (node) => {
  for (let n = node; n.parentNode; n = n.parentNode)
    if (n.nodeName.toLowerCase() === "a") return n;
  return null;
};
```

To test this function, use the following code:

```js
findClosestAnchor(document.querySelector("a > span")); // a
```
