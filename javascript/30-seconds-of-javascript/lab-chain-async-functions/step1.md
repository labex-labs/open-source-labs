# Chaining Asynchronous Functions

To chain asynchronous functions, open the Terminal/SSH and type `node`. Then, loop through an array of functions containing asynchronous events, and call the `next` function when each asynchronous event has completed.

Here's a code snippet that demonstrates how to chain asynchronous functions:

```js
const chainAsync = (fns) => {
  let curr = 0;
  const last = fns[fns.length - 1];
  const next = () => {
    const fn = fns[curr++];
    fn === last ? fn() : fn(next);
  };
  next();
};

chainAsync([
  (next) => {
    console.log("0 seconds");
    setTimeout(next, 1000);
  },
  (next) => {
    console.log("1 second");
    setTimeout(next, 1000);
  },
  () => {
    console.log("2 second");
  }
]);
```
