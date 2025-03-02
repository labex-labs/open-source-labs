# Преобразование значений в массивы в JavaScript

Для преобразования значения в массив используйте функцию `castArray`, предоставленную ниже.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

Для использования этой функции передайте в качестве аргумента значение, которое вы хотите преобразовать. Функция проверит, является ли значение уже массивом с использованием `Array.isArray()`. Если это массив, функция вернет его без изменений. Если это не массив, функция вернет значение, заключенное в массив.

Вот пример использования `castArray`:

```js
castArray("foo"); // возвращает: ['foo']
castArray([1]); // возвращает: [1]
```

Для начала практики программирования на JavaScript откройте Терминал или SSH и введите `node`.
