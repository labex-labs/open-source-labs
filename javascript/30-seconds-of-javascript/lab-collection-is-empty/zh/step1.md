# 检查集合是否为空

要检查一个集合是否为空，你可以打开终端/SSH 并输入 `node`。这个程序会检查一个值是否为空对象/集合、是否没有可枚举属性，或者是否是任何不被视为集合的类型。

要使用这个程序，检查提供的值是否为 `null` 或者其 `length` 是否等于 `0`。以下是一个示例代码：

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

然后你可以使用以下代码测试这个程序：

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - 类型不被视为集合
isEmpty(true); // true - 类型不被视为集合
```
