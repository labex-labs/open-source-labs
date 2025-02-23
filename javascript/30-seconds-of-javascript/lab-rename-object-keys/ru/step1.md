# Как переименовать ключи объектов в JavaScript

Для переименования нескольких ключей объекта с использованием предоставленных значений вы можете использовать функцию `renameKeys`. Вот шаги, которые необходимо выполнить:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте `Object.keys()` в сочетании с `Array.prototype.reduce()` и оператором расширения (`...`), чтобы получить ключи объекта и переименовать их в соответствии с `keysMap`.
3. Передайте `keysMap` и объект (`obj`) в качестве аргументов функции `renameKeys`.
4. Функция `renameKeys` возвращает новый объект с переименованными ключами.

Вот пример использования функции `renameKeys`:

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
