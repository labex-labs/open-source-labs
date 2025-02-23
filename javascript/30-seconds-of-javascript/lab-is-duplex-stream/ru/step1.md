# Проверка, является ли поток двусторонним

Для проверки, является ли поток двусторонним (читаемым и записываемым), откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода. Затем следуйте шагам:

1. Проверьте, отличается ли заданный аргумент от `null`.
2. Используйте `typeof`, чтобы проверить, является ли заданный аргумент объектом и имеет ли он свойство `pipe` типа `function`.
3. Кроме того, проверьте, являются ли свойства `_read`, `_write`, `_readableState` и `_writableState` типа `function` и `object` соответственно.

Вот код:

```js
const isDuplexStream = (val) =>
  val !== null &&
  typeof val === "object" &&
  typeof val.pipe === "function" &&
  typeof val._read === "function" &&
  typeof val._readableState === "object" &&
  typeof val._write === "function" &&
  typeof val._writableState === "object";
```

Вы можете протестировать этот код с использованием следующего примера:

```js
const Stream = require("stream");

isDuplexStream(new Stream.Duplex()); // true
```
