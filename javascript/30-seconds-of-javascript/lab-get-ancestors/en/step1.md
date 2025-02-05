# Retrieve Element Ancestors

To retrieve the ancestors of an element from the document root to the specified element, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Node.parentNode` and a `while` loop to move up the ancestor tree of the element.
3. Use `Array.prototype.unshift()` to add each new ancestor to the start of the array.

Here's a sample code that implements the above steps:

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

To retrieve the ancestors of a specific element, use the `querySelector()` method to select the element and pass it as an argument to the `getAncestors()` function. For example:

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

This will return an array of all ancestors of the specified element in the order from the document root to the element itself.
