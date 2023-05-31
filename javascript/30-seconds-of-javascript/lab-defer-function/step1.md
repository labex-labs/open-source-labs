# Deferring Function Invocation

To defer invoking a function until the current call stack has cleared, you can use the `setTimeout()` function with a timeout of `1` ms to add a new event to the event queue. This allows the rendering engine to complete its work. You can also use the spread (`...`) operator to supply the function with an arbitrary number of arguments.

Here's an example implementation of `defer`:

```js
const defer = (fn, ...args) => setTimeout(fn, 1, ...args);
```

You can use `defer` in situations where you want to prioritize the rendering of the page before running a long-running function. For example:

```js
// Example A:
defer(console.log, "a"), console.log("b"); // logs 'b' then 'a'

// Example B:
document.querySelector("#someElement").innerHTML = "Hello";
longRunningFunction();
// Browser will not update the HTML until this has finished
defer(longRunningFunction);
// Browser will update the HTML then run the function
```

In Example A, the `console.log('b')` statement is executed immediately, but the `console.log('a')` statement is deferred until the rendering engine has completed its work. This results in the output of `'b'` before `'a'`.

In Example B, the `longRunningFunction()` is deferred until after the HTML has been updated. This ensures that the user sees the updated HTML before the function starts running.
