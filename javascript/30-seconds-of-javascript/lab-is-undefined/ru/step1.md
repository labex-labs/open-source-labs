# Проверка на неопределенное значение

Для проверки того, является ли значение неопределенным, откройте Терминал/SSH и введите `node`.

- Используйте оператор строгого равенства для проверки, равно ли `val` `undefined`.

```js
const isUndefined = (val) => val === undefined;
```

```js
isUndefined(undefined); // true
```

Этот код проверит, является ли указанное значение неопределенным.
