# Running Promises in a Series

To execute an array of promises in a series, use `Array.prototype.reduce()` to create a promise chain. Each promise returns the next promise after being resolved.

To start, open the Terminal/SSH and type `node` to begin practicing coding.

Here's an example of the code:

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

You can then use the `runPromisesInSeries` function to execute promises sequentially, as shown in the following example:

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// This code runs each promise sequentially, taking a total of 3 seconds to complete.
```
