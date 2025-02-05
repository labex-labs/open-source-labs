# 将表单转换为对象

为了练习编码，打开终端/SSH 并输入 `node`。你可以通过以下步骤将一组表单元素编码为一个对象：

1. 使用 `FormData` 构造函数将 HTML `form` 转换为 `FormData`。
2. 使用 `Array.from()` 将 `FormData` 转换为数组。
3. 使用 `Array.prototype.reduce()` 从数组中收集对象。

以下是一个示例代码片段：

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

要转换特定的表单，你可以调用 `formToObject` 函数并将表单元素作为参数传入：

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
