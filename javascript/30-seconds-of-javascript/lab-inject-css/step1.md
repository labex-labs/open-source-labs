# How to Inject CSS into a Document

To inject CSS into a document, use the following steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a new `style` element using `Document.createElement()`, and set its type to `text/css`.
3. Use `Element.innerText` to set the value to the given CSS string.
4. Use `Document.head` and `Element.appendChild()` to append the new element to the document head.
5. Return the newly created `style` element.

Here is an example of how to use the `injectCSS` function to inject CSS code into a document:

```js
const injectCSS = (css) => {
  let el = document.createElement("style");
  el.type = "text/css";
  el.innerText = css;
  document.head.appendChild(el);
  return el;
};

injectCSS("body { background-color: #000 }");
// '<style type="text/css">body { background-color: #000 }</style>'
```
