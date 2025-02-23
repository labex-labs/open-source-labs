# Инструкции по переносу строки в строке

Для практики программирования откройте Терминал/SSH и введите `node`.

Этот код переносит строку до заданного количества символов с использованием символа переноса строки. Чтобы использовать его, следуйте шагам:

1. Используйте `String.prototype.replace()` и регулярное выражение для вставки заданного символа переноса в ближайшее пробел в строке длиной `max` символов.
2. Если вы не хотите использовать значение по умолчанию `'\n'` для третьего аргумента, `br`, вы можете его опустить и указать собственный символ.

Вот код:

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

Вот несколько примеров использования:

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
