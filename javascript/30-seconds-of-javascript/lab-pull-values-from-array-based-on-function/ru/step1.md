# Как извлекать значения из массива на основе заданной функции

Для начала практики программирования откройте Терминал/SSH и введите `node`.

Функция `pullBy` изменяет исходный массив, фильтруя указанные значения на основе заданной итераторной функции. Вот, как это работает:

1. Проверьте, является ли последний переданный аргумент функцией.
2. Используйте `Array.prototype.map()`, чтобы применить итераторную функцию `fn` ко всем элементам массива.
3. Используйте `Array.prototype.filter()` и `Array.prototype.includes()`, чтобы извлечь ненужные значения.
4. Установите `Array.prototype.length`, чтобы сбросить длину переданного массива до `0`.
5. Используйте `Array.prototype.push()`, чтобы заполнить его только извлеченными значениями.

Вот код:

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

Вот пример использования:

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

Обратите внимание, что в этом примере мы извлекаем все элементы с свойством `x`, равным `1` или `3`. Результирующий `myArray` будет содержать только элемент с свойством `x`, равным `2`.
