# Как сериализовать циклический JSON

Для сериализации JSON-объекта, содержащего циклические ссылки, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Создайте `WeakSet`, чтобы хранить и проверять уже виденные значения с использованием `WeakSet.prototype.add()` и `WeakSet.prototype.has()`.
3. Используйте `JSON.stringify()` с пользовательской функцией-заменителем, которая пропускает значения, уже присутствующие в `seen`, и добавляет новые значения при необходимости.
4. ⚠️ **ВНИМАНИЕ:** Эта функция находит и удаляет циклические ссылки, что приводит к потере циклических данных в сериализованном JSON.

Вот код для функции `stringifyCircularJSON`:

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

Для тестирования функции вы можете создать объект с циклической ссылкой и вызвать `stringifyCircularJSON`:

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
