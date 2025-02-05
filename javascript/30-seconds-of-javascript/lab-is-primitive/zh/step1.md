# 检查原始值

为了练习编码，打开终端或 SSH 并输入 `node`。完成此操作后，你可以通过以下步骤检查一个值是否为原始值：

1. 使用 `Object(val)` 从你要检查的值创建一个对象。
2. 使用严格不等运算符 `!==` 将创建的对象与原始值进行比较。
3. 如果两个值不相等，则原始值是原始值。

以下是 `isPrimitive` 函数的代码：

```js
const isPrimitive = (val) => Object(val) !== val;
```

你可以使用以下值测试此函数：

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

如果你要检查的值是原始值，该函数将返回 `true`。否则，它将返回 `false`。
