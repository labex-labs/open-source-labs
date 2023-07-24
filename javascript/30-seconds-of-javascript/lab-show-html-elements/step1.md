# How to Show Elements

To display all the specified elements, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Use the spread operator (`...`) and `Array.prototype.forEach()` to clear the `display` property for each specified element.
4. Use the `show()` function provided in the code snippet below.

```js
const show = (...el) => [...el].forEach((e) => (e.style.display = ""));
```

For example, to show all `<img>` elements on the page, use the following code:

```js
show(...document.querySelectorAll("img"));
```
