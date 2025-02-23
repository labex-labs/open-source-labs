# Проверка, является ли поток записываемым

Для проверки, является ли поток записываемым, откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода. Затем следуйте шагам:

1. Проверьте, что заданный аргумент не равен `null`.
2. Используйте `typeof`, чтобы проверить, является ли значение `object` и является ли свойство `pipe` `function`.
3. Кроме того, проверьте, что `typeof` свойств `_write` и `_writableState` равны `function` и `object` соответственно.

Вот пример кода, который реализует эти проверки:

```js
const isWritableStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Вы можете протестировать эту функцию с использованием модуля `fs` в Node.js. Например:

```js
const fs = require("fs");

isWritableStream(fs.createWriteStream("test.txt")); // true
```
