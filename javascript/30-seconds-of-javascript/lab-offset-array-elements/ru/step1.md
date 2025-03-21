# Как смещать элементы массива в JavaScript

Для перемещения указанного количества элементов в конец массива JavaScript выполните следующие шаги:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте метод `Array.prototype.slice()` дважды, чтобы получить элементы после указанного индекса и элементы перед ним.
3. Используйте оператор расширения (`...`), чтобы объединить два массива в один.
4. Если `offset` отрицательный, элементы будут перемещены с конца массива в начало.

Вот пример кода, который реализует функцию `offset`:

```js
const offset = (arr, offset) => [...arr.slice(offset), ...arr.slice(0, offset)];
```

Затем вы можете вызвать функцию с желаемыми значениями массива и смещения:

```js
offset([1, 2, 3, 4, 5], 2); // [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2); // [4, 5, 1, 2, 3]
```
