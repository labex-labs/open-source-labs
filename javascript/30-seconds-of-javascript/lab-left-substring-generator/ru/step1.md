# Практика кода: Генератор левых подстрок

Для генерации всех левых подстрок заданной строки используйте функцию `leftSubstrGenerator`, предоставленную ниже.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

Для использования функции откройте Терминал/SSH и введите `node`. Затем введите функцию с аргументом-строкой:

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

Функция использует `String.prototype.length` для раннего завершения, если строка пуста, и цикл `for...in` с `String.prototype.slice()`, чтобы `возвращать` каждую подстроку заданной строки, начиная с начала.
