# Function to Find Closest Matching Node

To find the closest matching node starting at the given `node`, use the following function:

```js
const findClosestMatchingNode = (node, selector) => {
  for (let n = node; n.parentNode; n = n.parentNode)
    if (n.matches && n.matches(selector)) return n;
  return null;
};
```

To use the function, provide the starting `node` and the `selector` to match against. The function will use a `for` loop and `Node.parentNode` to traverse the node tree upwards from the given `node`. It will then use `Element.matches()` to check if any given element node matches the provided `selector`. If no matching node is found, the function will return `null`.

Example usage:

```js
findClosestMatchingNode(document.querySelector("span"), "body"); // returns body
```
