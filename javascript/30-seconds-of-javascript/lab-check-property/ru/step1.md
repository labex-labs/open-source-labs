# Проверка свойства

Для проверки того, соответствует ли определенное свойство объекта определенному условию, используйте функцию `checkProp`. Эта функция создает каррированную функцию, которая принимает в качестве аргументов предикат-функцию и имя свойства. Возвращенная функция затем принимает объект и возвращает `true` или `false` в зависимости от того, соответствует ли указанное свойство условию, заданному предикат-функцией.

Вот пример реализации `checkProp`:

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

И вот несколько примеров использования этой функции:

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set использует Size, а не length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

Кратко говоря, функция `checkProp` позволяет легко проверить значение определенного свойства на объекте, указав для этого свойства предикат-функцию.
