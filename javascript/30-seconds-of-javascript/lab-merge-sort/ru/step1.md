# Алгоритм сортировки слиянием

Для практики программирования с использованием алгоритма сортировки слиянием выполните следующие шаги:

1. Откройте Терминал/SSH и введите `node`.
2. Используйте рекурсию для сортировки массива чисел.
3. Если `длина` массива меньше `2`, верните массив.
4. Используйте `Math.floor()` для вычисления середины массива.
5. Используйте `Array.prototype.slice()` для разделения массива на две части и рекурсивно вызовите `mergeSort()` для созданных подмассивов.
6. Наконец, используйте `Array.from()` и `Array.prototype.shift()` для объединения двух отсортированных подмассивов в один.

Вот код:

```js
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const mid = Math.floor(arr.length / 2);
  const l = mergeSort(arr.slice(0, mid));
  const r = mergeSort(arr.slice(mid, arr.length));
  return Array.from({ length: l.length + r.length }, () => {
    if (!l.length) return r.shift();
    else if (!r.length) return l.shift();
    else return l[0] > r[0] ? r.shift() : l.shift();
  });
};
```

Попробуйте его на этом примере:

```js
mergeSort([5, 1, 4, 2, 3]); // [1, 2, 3, 4, 5]
```
