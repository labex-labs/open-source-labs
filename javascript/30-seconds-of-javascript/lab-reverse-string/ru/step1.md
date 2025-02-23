# Вот функция для переворота строки:

Для переворота строки используйте оператор расширения (`...`) и `Array.prototype.reverse()`. Объедините символы, чтобы получить строку, используя `Array.prototype.join()`. Вот код:

```js
const reverseString = (str) => [...str].reverse().join("");
```

Пример использования:

```js
reverseString("foobar"); // 'raboof'
```
