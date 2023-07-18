# Checking User's Dark Color Scheme Preference

To check if the user prefers a dark color scheme, use `Window.matchMedia()` with the appropriate media query.

```js
const prefersDarkColorScheme = () =>
  window &&
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches;
```

To start practicing coding, open the Terminal/SSH and type `node`.

Example usage:

```js
prefersDarkColorScheme(); // true
```
