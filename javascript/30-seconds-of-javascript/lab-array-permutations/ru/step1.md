# Как сгенерировать все перестановки массива

Для начала практики в программировании откройте Терминал/SSH и введите `node`.

Вот алгоритм, который генерирует все перестановки элементов массива (даже если он содержит дубликаты). Следуйте шагам для его реализации:

1. Используйте рекурсию.
2. Для каждого элемента в заданном массиве создайте все частичные перестановки для остальных его элементов.
3. Используйте `Array.prototype.map()`, чтобы объединить элемент с каждой частичной перестановкой, а затем `Array.prototype.reduce()`, чтобы объединить все перестановки в один массив.
4. Базовыми случаями являются массивы длиной `2` или `1`.
5. Будьте осторожны, так как время выполнения этой функции увеличивается экспоненциально с каждым элементом массива. Больше 8 - 10 элементов может привести к зависанию вашего браузера, когда он пытается решить все разные комбинации.

Вот код:

```js
const permutations = (arr) => {
  if (arr.length <= 2) return arr.length === 2 ? [arr, [arr[1], arr[0]]] : arr;
  return arr.reduce(
    (acc, item, i) =>
      acc.concat(
        permutations([...arr.slice(0, i), ...arr.slice(i + 1)]).map((val) => [
          item,
          ...val
        ])
      ),
    []
  );
};
```

Вы можете протестировать код, вызвав функцию `permutations()` с аргументом массива:

```js
permutations([1, 33, 5]);
// [ [1, 33, 5], [1, 5, 33], [33, 1, 5], [33, 5, 1], [5, 1, 33], [5, 33, 1] ]
```
