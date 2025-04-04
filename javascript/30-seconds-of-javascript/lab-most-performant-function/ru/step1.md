# Как найти самую производительную функцию в JavaScript

Чтобы найти самую производительную функцию в JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковать программирование.
2. Используйте `Array.prototype.map()`, чтобы сгенерировать массив, где каждое значение — это общее время выполнения функции после `iterations` раз.
3. Используйте разницу между значениями `performance.now()` до и после выполнения, чтобы получить общее время в миллисекундах с высокой степенью точности.
4. Используйте `Math.min()`, чтобы найти минимальное время выполнения, и верните индекс этого самого короткого времени, который соответствует индексу самой производительной функции.
5. Если вы опустите второй аргумент, `iterations`, функция будет использовать значение по умолчанию `10000` итераций. 6.牢记，使用的迭代次数越多，结果就越可靠，但所需的时间也就越长。

Вот пример кода:

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

Чтобы использовать эту функцию, передайте массив функций в качестве первого аргумента и количество итераций в качестве второго аргумента (необязательно). Например:

```js
mostPerformant([
  () => {
    // Проходит по всему массиву перед возвратом `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Требуется только до индекса `1`, прежде чем вернуть `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
