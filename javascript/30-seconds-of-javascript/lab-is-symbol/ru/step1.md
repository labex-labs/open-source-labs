# Проверка, является ли значение символом в JavaScript

Чтобы проверить, является ли значение примитивным символом в JavaScript, можно использовать оператор `typeof`. Вот пример кода, который можно использовать:

```js
const isSymbol = (val) => typeof val === "symbol";
```

Можно вызвать функцию `isSymbol` и передать символ в качестве аргумента, чтобы проверить, возвращает ли она `true`. Вот пример:

```js
isSymbol(Symbol("x")); // true
```
