# Проверить, является ли поток читаемым

Для проверки того, является ли заданный аргумент читаемым потоком, следуйте следующим шагам:

- Во - первых, откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Проверьте, что значение не равно `null`.
- Используйте `typeof`, чтобы проверить, является ли значение `object`, а свойство `pipe` - `function`.
- Кроме того, проверьте, являются ли `typeof` свойств `_read` и `_readableState` соответственно `function` и `object`.

Вот пример функции, которая реализует эти шаги:

```js
const isReadableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object";
```

Вы можете использовать эту функцию для проверки того, является ли поток читаемым, следующим образом:

```js
const fs = require("fs");

isReadableStream(fs.createReadStream("test.txt")); // true
```
