# Как.deep freeze объект в JavaScript

Чтобы.deep freeze объект в JavaScript, следуйте следующим шагам:

1. Используйте `Object.keys()`, чтобы получить все свойства переданного объекта.
2. Перебирайте свойства с использованием `Array.prototype.forEach()`.
3. Рекурсивно вызовите `Object.freeze()` для всех свойств, которые являются объектами, применяя `deepFreeze()` при необходимости.
4. Наконец, используйте `Object.freeze()`, чтобы заморозить заданный объект.

Вот код:

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

Вы можете протестировать.deep frozen объект с использованием следующего кода:

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // не разрешается
val[1][0] = 4; // также не разрешается
```

Вышеприведенный код вызовет ошибку, так как объект `val`.deep frozen и не может быть модифицирован.
