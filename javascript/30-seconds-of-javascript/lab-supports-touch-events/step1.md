# Device Supports Touch Events

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if touch events are supported.

- Check if `'ontouchstart'` exists in the `Window`.

```js
const supportsTouchEvents = () =>
  window && 'ontouchstart' in window;
```

```js
supportsTouchEvents(); // true
```
