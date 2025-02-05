# 以下是将对象转换为 Map 的方法

要将对象转换为 `Map`，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.entries()` 将对象转换为键值对数组。
3. 使用 `Map` 构造函数将数组转换为 `Map`。

以下是一个示例代码片段：

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

你可以使用 `objectToMap()` 函数将对象转换为 `Map`。例如：

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
