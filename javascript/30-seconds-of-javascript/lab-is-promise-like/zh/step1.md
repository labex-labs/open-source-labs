# JavaScript 中的 Promise

要检查一个对象是否类似于 Promise，可以使用 `isPromiseLike` 函数。该函数会检查对象是否不为 null，是否是对象类型或函数类型，并且是否具有一个也是函数的 `.then` 属性。

以下是 `isPromiseLike` 的代码：

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

以下是一些使用 `isPromiseLike` 的示例：

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

要开始练习 JavaScript 编码，请打开终端/SSH 并输入 `node`。
