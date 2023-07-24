# Getting the Vertical Offset of an Element

To find the distance from a given element to the top of the document, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use the `while` loop and `HTMLElement.offsetParent` to move up the offset parents of the given element.

3. Add `HTMLElement.offsetTop` for each element and return the result.

Use the following code to get the vertical offset of an element:

```js
const getVerticalOffset = (el) => {
  let offset = el.offsetTop,
    _el = el;
  while (_el.offsetParent) {
    _el = _el.offsetParent;
    offset += _el.offsetTop;
  }
  return offset;
};

getVerticalOffset(".my-element"); // 120
```
