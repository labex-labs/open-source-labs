# Алгоритм сжатия объекта

Для глубокого удаления всех ложных значений из объекта или массива используйте следующий алгоритм:

1. Используйте рекурсию для вызова функции `compactObject()` для каждого вложенного объекта или массива.
2. Инициализируйте итерируемые данные с использованием `Array.isArray()`, `Array.prototype.filter()` и `Boolean()`. Это делается для избежания создания разреженных массивов.
3. Используйте `Object.keys()` и `Array.prototype.reduce()`, чтобы перебрать каждый ключ с соответствующим начальным значением.
4. Используйте `Boolean()`, чтобы определить истинность значения каждого ключа, и добавьте его в аккумулятор, если оно истинно.
5. Используйте `typeof`, чтобы определить, является ли заданное значение `object`, и вызовите функцию снова, чтобы глубоко сжать его.

Вот код функции `compactObject()`:

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

Для использования этой функции передайте объект или массив в качестве аргумента в `compactObject()`. Функция вернет новый объект или массив с удалеными всеми ложными значениями.

Например:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
