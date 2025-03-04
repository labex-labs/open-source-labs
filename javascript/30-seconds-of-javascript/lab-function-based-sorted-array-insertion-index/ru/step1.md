# Функция для нахождения индекса вставки в отсортированном массиве

Для нахождения наименьшего индекса для вставки значения в массив и сохранения его сортировки используйте функцию `sortedIndexBy(arr, n, fn)` в JavaScript.

Эта функция нестрого проверяет, отсортирован ли массив по убыванию, а затем использует `Array.prototype.findIndex()`, чтобы найти соответствующий индекс на основе итераторной функции `fn`.

Вот код функции `sortedIndexBy()`:

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

Вы можете вызвать функцию с массивом объектов, значением для вставки и итераторной функцией.

Например, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` возвращает `0`, что является индексом, где объект `{ x: 4 }` должен быть вставлен, чтобы сохранить сортировку по свойству `x`.
