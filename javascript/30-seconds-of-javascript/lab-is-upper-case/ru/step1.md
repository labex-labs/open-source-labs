# Функция для проверки, является ли строка полностью заглавной

Для проверки того, является ли строка полностью заглавной, следуйте шагам:

1. Откройте Терминал/SSH.
2. Введите `node`.
3. Используйте функцию `isUpperCase()` для преобразования заданной строки в верхний регистр с использованием `String.prototype.toUpperCase()` и сравните ее с исходной строкой.
4. Функция вернет `true`, если строка полностью заглавная, и `false`, если это не так.

Вот пример кода:

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
