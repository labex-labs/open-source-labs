# Как извлечь значения из массива по индексу

Для извлечения конкретных значений из массива по определенным индексам следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Array.prototype.filter()` и `Array.prototype.includes()` для фильтрации ненужных значений и сохраните их в новом массиве под названием `removed`.
3. Установите `Array.prototype.length` равным `0`, чтобы изменить исходный массив, сбросив его длину.
4. Используйте `Array.prototype.push()` для перезаполнения исходного массива только извлеченными значениями.
5. Используйте `Array.prototype.push()` для отслеживания удаленных значений.
6. Функция `pullAtIndex` принимает два аргумента: исходный массив и массив индексов для извлечения.
7. Функция возвращает массив удаленных значений.

Пример использования:

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
