# Функция для определения типа значения

Для определения типа значения используйте следующую функцию:

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- Функция возвращает `'undefined'` или `'null'`, если значение равно `undefined` или `null`.
- В противном случае она возвращает имя конструктора, используя `Object.prototype.constructor` и `Function.prototype.name`.

Пример использования:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
