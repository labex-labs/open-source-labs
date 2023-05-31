# User Prefers Dark Color Scheme

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if the user color scheme preference is `dark`.

- Use `Window.matchMedia()` with the appropriate media query to check the user color scheme preference.

```js
const prefersDarkColorScheme = () =>
  window &&
  window.matchMedia &&
  window.matchMedia('(prefers-color-scheme: dark)').matches;
```

```js
prefersDarkColorScheme(); // true
```
