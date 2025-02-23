# Функция для нормализации окончаний строк

Для нормализации окончаний строк в строке можно использовать следующую функцию.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Используйте `String.prototype.replace()` с регулярным выражением для сопоставления и замены окончаний строк на `normalized` версию.
- По умолчанию `normalized` версия установлена на `'\r\n'`.
- Чтобы использовать другую `normalized` версию, передайте ее в качестве второго аргумента.

Вот несколько примеров:

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
