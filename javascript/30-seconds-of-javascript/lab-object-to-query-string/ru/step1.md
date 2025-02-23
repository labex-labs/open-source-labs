# Преобразование объекта в строку запроса

Для преобразования объекта в строку запроса используйте функцию `objectToQueryString()`, которая генерирует строку запроса из пар ключ-значение заданного объекта.

Функция работает следующим образом:

- Она использует `Array.prototype.reduce()` для `Object.entries()` для создания строки запроса из `queryParameters`.
- Она определяет `symbol` как `?` или `&` в зависимости от длины `queryString`.
- Она конкатенирует `val` к `queryString` только если это строка.
- Она возвращает `queryString` или пустую строку, когда `queryParameters` ложны.

Вот код для функции `objectToQueryString()`:

```js
const objectToQueryString = (queryParameters) => {
  return queryParameters
    ? Object.entries(queryParameters).reduce(
        (queryString, [key, val], index) => {
          const symbol = queryString.length === 0 ? "?" : "&";
          queryString +=
            typeof val === "string" ? `${symbol}${key}=${val}` : "";
          return queryString;
        },
        ""
      )
    : "";
};
```

Пример использования функции `objectToQueryString()`:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // возвращает '?page=1&size=2kg'
```
