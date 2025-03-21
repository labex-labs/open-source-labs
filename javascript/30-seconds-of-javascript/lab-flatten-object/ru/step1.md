# Сглаживание объекта

Чтобы сгладить объект с путями для ключей, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте рекурсию для сглаживания объекта.
3. Используйте `Object.keys()`, комбинированное с `Array.prototype.reduce()`, чтобы преобразовать каждый лист в узел с сглаженным путём.
4. Если значение ключа является объектом, вызовите функцию рекурсивно с соответствующим `prefix`, чтобы создать путь с использованием `Object.assign()`.
5. В противном случае добавьте соответствующую пару ключ-значение с префиксом в объект-аккумулятор.
6. Игнорируйте второй аргумент, `prefix`, если вы не хотите, чтобы каждый ключ имел префикс.

Вот пример реализации:

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

Вы можете использовать функцию `flattenObject` так:

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
