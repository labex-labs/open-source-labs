# How to Toggle Fullscreen Mode in JavaScript

To start practicing coding in JavaScript, open the Terminal/SSH and type `node`. Once you're ready to toggle fullscreen mode, you can use the following code:

```js
const fullscreen = (mode = true, el = "body") => {
  const element = document.querySelector(el);
  if (mode) {
    element.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
};
```

The function `fullscreen` accepts two optional arguments: `mode` and `el`. By default, it opens the `body` element in fullscreen mode. If you want to specify a different element, you can pass a CSS selector as the second argument.

Here are some examples of how to use the `fullscreen` function:

```js
fullscreen(); // Opens `body` in fullscreen mode
fullscreen(false); // Exits fullscreen mode
fullscreen(true, "#my-element"); // Opens `#my-element` in fullscreen mode
```
