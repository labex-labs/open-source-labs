# Как проверить, является ли значение null или undefined в JavaScript

Для определения того, является ли значение `null` или `undefined` в JavaScript, можно использовать строгое равенство (`===`). Вот пример кода, который проверяет, является ли указанное значение `null` или `undefined`:

```js
const isNil = (val) => val === undefined || val === null;
```

Можно использовать эту функцию для проверки, является ли значение `null` или `undefined`, следующим образом:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

Для начала практики программирования на JavaScript можно открыть Терминал/SSH и ввести `node`.
