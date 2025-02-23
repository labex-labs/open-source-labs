# Генерация UUID в Node.js

Чтобы сгенерировать UUID в Node.js, следуйте шагам ниже:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте метод `crypto.randomBytes()` для генерации UUID, соответствующего [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) версии 4.
3. Преобразуйте сгенерированный UUID в правильный UUID (шестнадцатеричную строку) с использованием метода `Number.prototype.toString()`.
4. Альтернативно вы можете использовать метод [`crypto.randomUUID()`](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions), который предоставляет аналогичную функциональность.

Вот пример кода для генерации UUID в Node.js:

```js
const crypto = require("crypto");

const UUIDGeneratorNode = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (c ^ (crypto.randomBytes(1)[0] & (15 >> (c / 4)))).toString(16)
  );
```

Вы можете вызвать метод `UUIDGeneratorNode()`, чтобы сгенерировать UUID.

```js
UUIDGeneratorNode(); // '79c7c136-60ee-40a2-beb2-856f1feabefc'
```
