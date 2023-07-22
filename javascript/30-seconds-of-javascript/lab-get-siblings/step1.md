# A Function to Get an Array of Element's Siblings

To get an array containing all the siblings of a particular element, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Node.parentNode` and `Node.childNodes` properties to get a `NodeList` of all the elements that are contained in the element's parent.
3. Use the spread operator (`...`) and `Array.prototype.filter()` to convert this `NodeList` to an array and remove the given element from it.
4. Define a function that takes an element as its argument and returns an array of its siblings using the above steps.

Here's the function:

```js
const getSiblings = (el) =>
  [...el.parentNode.childNodes].filter((node) => node !== el);
```

You can call this function with a selector to get an array of siblings for a particular element. For example:

```js
getSiblings(document.querySelector("head")); // ['body']
```
