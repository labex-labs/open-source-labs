# Функция для преобразования символов в строке

Для использования этой функции для преобразования символов в строке выполните следующие шаги:

- Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Используйте `String.prototype.split()` и `Array.prototype.map()`, чтобы вызвать предоставленную функцию `fn` для каждого символа в заданной строке.
- Используйте `Array.prototype.join()`, чтобы снова объединить массив символов в новую строку.
- Функция обратного вызова `fn` принимает три аргумента: текущий символ, индекс текущего символа и строку, для которой была вызвана `mapString`.

Вот код функции:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Пример использования:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
