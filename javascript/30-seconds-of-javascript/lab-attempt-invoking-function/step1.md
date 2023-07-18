# Function Invocation and Error Handling

To invoke a function with arguments, open the Terminal/SSH and type `node`. Once you have done that, you can use the following code to attempt invoking the function and handle any possible errors:

```js
const attempt = (fn, ...args) => {
  try {
    return fn(...args);
  } catch (e) {
    return e instanceof Error ? e : new Error(e);
  }
};
```

Here are some guidelines for using the `attempt` function:

- Pass the function you want to invoke and its arguments as parameters.
- Use a `try...catch` block to handle any errors that occur during the function invocation.
- If an error is caught, check if it is an instance of the `Error` object. If not, create a new `Error` object.
- Use the returned value to either get the result of the function or an appropriate error object.

Here is an example of how you can use the `attempt` function:

```js
var elements = attempt(function (selector) {
  return document.querySelectorAll(selector);
}, ">_>");
if (elements instanceof Error) elements = []; // elements = []
```

In this example, the `attempt` function is used to invoke the `document.querySelectorAll` function with the `'>_>'` selector. If an error occurs, the `elements` variable will be set to an empty array.
