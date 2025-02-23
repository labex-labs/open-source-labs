# Удаление диакритических знаков

Эта функция удаляет диакритические знаки из строк.

- Используйте `String.prototype.normalize()`, чтобы преобразовать строку в нормализованный формат Unicode.
- Используйте `String.prototype.replace()`, чтобы заменить диакритические знаки в заданном диапазоне Unicode на пустые строки.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

Для использования этой функции откройте Терминал/SSH и введите `node`. Затем вызовите функцию с аргументом в виде строки.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
