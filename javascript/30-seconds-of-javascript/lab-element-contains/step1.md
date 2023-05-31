# Checking if an Element Contains Another Element

To check if an element contains another element:

1. Ensure that the parent element and child element are not the same.
2. Use the `Node.contains()` method to check if the parent element contains the child element.

Here's an example code snippet:

```js
const elementContains = (parent, child) =>
  parent !== child && parent.contains(child);
```

You can then use the `elementContains()` function to check if an element contains another element, as shown below:

```js
elementContains(
  document.querySelector("head"),
  document.querySelector("title")
); // true

elementContains(document.querySelector("body"), document.querySelector("body")); // false
```
