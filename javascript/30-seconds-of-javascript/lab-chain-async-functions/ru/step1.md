# Последовательное выполнение асинхронных функций

Для последовательного выполнения асинхронных функций откройте Терминал/SSH и введите `node`. Затем пройдите по массиву функций, содержащих асинхронные события, и вызовите функцию `next`, когда каждое асинхронное событие завершится.

Вот фрагмент кода, демонстрирующий, как последовательно выполнять асинхронные функции:

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
