# Как задержать выполнение асинхронной функции в JavaScript

Чтобы задержать выполнение асинхронной функции в JavaScript, вы можете использовать функцию `sleep` ниже, которая возвращает `Promise`, которое разрешается через определенное время. Вот пример того, как задержать выполнение части `async`-функции с использованием `sleep`:

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function sleepyWork() {
  console.log("I'm going to sleep for 1 second.");
  await sleep(1000);
  console.log("I woke up after 1 second.");
}
```

Для использования этой функции просто вызовите `sleepyWork()`, и консоль выведет сообщения с задержкой в 1 секунду между ними.
