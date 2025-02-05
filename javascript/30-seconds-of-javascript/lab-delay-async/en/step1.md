# How to Delay Execution of an Async Function in JavaScript

To delay the execution of an asynchronous function in JavaScript, you can use the `sleep` function below, which returns a `Promise` that resolves after a certain amount of time. Here's an example of how to delay the execution of part of an `async` function using `sleep`:

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("I'm going to sleep for 1 second.");
  await sleep(1000);
  console.log("I woke up after 1 second.");
}
```

To use this function, simply call `sleepyWork()` and the console will log the messages with a 1 second delay between them.
