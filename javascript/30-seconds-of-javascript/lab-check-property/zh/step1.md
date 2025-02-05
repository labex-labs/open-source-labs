# 属性检查器

要检查对象的特定属性是否满足某个条件，请使用 `checkProp` 函数。此函数创建一个柯里化函数，该函数接受一个谓词函数和一个属性名作为参数。然后，返回的函数接受一个对象，并根据指定的属性是否满足谓词函数指定的条件返回 `true` 或 `false`。

以下是 `checkProp` 的示例实现：

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

以下是一些使用它的示例：

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set 使用 Size，而不是 length)

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

总之，`checkProp` 函数允许你通过为特定属性指定谓词函数来轻松检查对象上该属性的值。
