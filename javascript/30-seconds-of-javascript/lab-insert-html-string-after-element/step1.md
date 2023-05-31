# How to Insert HTML String After an Element in JavaScript

To insert an HTML string after the end of a specified element in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to begin practicing coding.
2. Use the `Element.insertAdjacentHTML()` method with a position of `'afterend'`.
3. Pass the `el` and `htmlString` parameters to the `insertAdjacentHTML()` method.
4. The `htmlString` parameter will be parsed and inserted after the end of the `el` element.

Here's an example of the `insertAfter` function in action:

```js
const insertAfter = (el, htmlString) =>
  el.insertAdjacentHTML("afterend", htmlString);

insertAfter(document.getElementById("myId"), "<p>after</p>");
// <div id="myId">...</div> <p>after</p>
```

In the example above, the `insertAfter` function is called with the `el` parameter set to the element with an ID of `myId` and the `htmlString` parameter set to `<p>after</p>`. The resulting HTML output will insert the `<p>` tag after the `myId` element.
