# Как извлечь соответствующие значения из массива

Чтобы извлечь конкретные значения из массива с использованием JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Array.prototype.filter()` и `Array.prototype.includes()` для фильтрации ненужных значений и создания нового массива.
3. Установите `Array.prototype.length`, чтобы изменить исходный массив, сбросив его длину до `0`.
4. Используйте `Array.prototype.push()`, чтобы заполнить исходный массив только извлеченными значениями.
5. Используйте `Array.prototype.push()`, чтобы отслеживать удаленные значения в новом массиве.

Вот пример функции, которая реализует эти шаги:

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

Вы можете использовать эту функцию для удаления конкретных значений из массива и возврата удаленных элементов так:

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
