# JavaScript function to get all parents of an element until a matching selector is found

To start practicing coding, open the Terminal/SSH and type `node`.

This function finds all the ancestor elements of a given element up until the element that matches the specified selector.

To achieve this, the function does the following:

- It uses `Node.parentNode` and a `while` loop to traverse the ancestor tree of the element.
- It uses `Array.prototype.unshift()` to add each new ancestor to the start of the array.
- It uses `Element.matches()` to check if the current element matches the specified `selector`.

Here's the code for the function:

```js
const getParentsUntil = (el, selector) => {
  let parents = [],
    _el = el.parentNode;
  while (_el && typeof _el.matches === "function") {
    parents.unshift(_el);
    if (_el.matches(selector)) return parents;
    else _el = _el.parentNode;
  }
  return [];
};
```

You can use the function like this:

```js
getParentsUntil(document.querySelector("#home-link"), "header");
// [header, nav, ul, li]
```
