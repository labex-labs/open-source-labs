# Handling User Input Change

To start practicing coding, open the Terminal/SSH and type `node`. This code runs the callback whenever the user input type changes (`mouse` or `touch`). It uses two event listeners and assumes `mouse` input initially, binding a `'touchstart'` event listener to the document. On `'touchstart'`, it adds a `'mousemove'` event listener to listen for two consecutive `'mousemove'` events firing within 20ms, using `performance.now()`. It runs the callback with the input type as an argument in either of these situations.

```js
const onUserInputChange = (callback) => {
  let type = "mouse",
    lastTime = 0;
  const mousemoveHandler = () => {
    const now = performance.now();
    if (now - lastTime < 20)
      (type = "mouse"),
        callback(type),
        document.removeEventListener("mousemove", mousemoveHandler);
    lastTime = now;
  };
  document.addEventListener("touchstart", () => {
    if (type === "touch") return;
    (type = "touch"),
      callback(type),
      document.addEventListener("mousemove", mousemoveHandler);
  });
};
```

To test the code, use this function:

```js
onUserInputChange((type) => {
  console.log("The user is now using", type, "as an input method.");
});
```
