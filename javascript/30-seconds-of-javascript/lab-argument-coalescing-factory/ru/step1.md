# Код фабрики для слияния аргументов

Для начала работы с кодом откройте Терминал/SSH и введите `node`. Эта функция возвращает первый аргумент, который оценивается как `истинно` на основе переданного валидатора в качестве аргумента.

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

Используйте `Array.prototype.find()`, чтобы вернуть первый аргумент, который возвращает `истинно` из предоставленной функции проверки аргументов `valid`. Например,

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

Здесь функция `coalesceFactory` настраивается для создания функции `customCoalesce`. Функция `customCoalesce` фильтрует `null`, `undefined`, `NaN` и пустые строки из предоставленных аргументов и возвращает первый аргумент, который не был отфильтрован. Результатом `customCoalesce(undefined, null, NaN, '', 'Waldo')` является `'Waldo'`.
