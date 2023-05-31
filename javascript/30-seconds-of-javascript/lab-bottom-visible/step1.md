# Check if Bottom of Page Is Visible

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if the bottom of the page is visible.

- Use `Window.scrollY`, `Element.scrollHeight` and `Element.clientHeight` to determine if the bottom of the page is visible.

```js
const bottomVisible = () =>
  document.documentElement.clientHeight + window.scrollY >=
  (document.documentElement.scrollHeight ||
    document.documentElement.clientHeight);
```

```js
bottomVisible(); // true
```
