# Проверить, является ли значение похожим на массив

Для проверки того, является ли значение похожим на массив, следуйте следующим шагам:

1. Откройте Терминал/SSH.
2. Введите `node`.
3. Используйте следующий код для проверки того, является ли переданный аргумент итерируемым:

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. Функция вернет `true`, если переданный аргумент является объектом, похожим на массив, и `false` в противном случае.
5. Например:

```js
isArrayLike([1, 2, 3]); // true
isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
