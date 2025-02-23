# Функция для сжатия пробелов в строке

Для сжатия пробелов в строке используйте функцию `compactWhitespace()`.

- Она использует `String.prototype.replace()` с регулярным выражением для замены всех вхождений 2 и более пробельных символов на один пробел.
- Функция принимает строку в качестве аргумента и возвращает сжатую строку.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Пример использования:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
