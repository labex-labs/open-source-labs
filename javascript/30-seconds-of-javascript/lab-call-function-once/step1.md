# Ensuring a Function is Called Only Once

To ensure that a function is called only once, you can use the `once` function. To start practicing coding, open the Terminal/SSH and type `node`. The `once` function utilizes a closure and a flag named `called`. The flag is set to `true` once the function is called for the first time, preventing it from being called again.

In order to allow the function to have its `this` context changed, such as in an event listener, you must use the `function` keyword. The supplied function must have the context applied. Additionally, the function can be supplied with an arbitrary number of arguments using the rest/spread (`...`) operator.

Here is an example implementation of the `once` function:

```js
const once = (fn) => {
  let called = false;
  return function (...args) {
    if (called) return;
    called = true;
    return fn.apply(this, args);
  };
};
```

You can use the `once` function to call a function only once, like this:

```js
const startApp = function (event) {
  console.log(this, event); // document.body, MouseEvent
};
document.body.addEventListener("click", once(startApp));
// only runs `startApp` once upon click
```
