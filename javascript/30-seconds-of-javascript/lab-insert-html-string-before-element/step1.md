# How to Insert an HTML String Before an Element in JavaScript

To insert an HTML string before a specified element in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Element.insertAdjacentHTML()` method with a position of `'beforebegin'`.
3. Pass in the HTML string that you want to insert before the element.
4. Pass in the element that you want to insert the HTML string before.

Here is an example code snippet:

```js
const insertBefore = (el, htmlString) =>
  el.insertAdjacentHTML("beforebegin", htmlString);

insertBefore(document.getElementById("myId"), "<p>before</p>");
// Output: <p>before</p> <div id="myId">...</div>
```

In the above example, the `insertBefore()` function takes two parameters: the element to insert the HTML before (`el`) and the HTML string to insert (`htmlString`). The `insertAdjacentHTML()` method is then called on the element with a position of `'beforebegin'` to insert the HTML before the element.
