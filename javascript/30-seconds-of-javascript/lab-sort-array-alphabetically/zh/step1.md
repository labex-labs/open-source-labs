# 如何在 JavaScript 中根据给定属性按字母顺序对数组进行排序

要在 JavaScript 中根据给定属性按字母顺序对对象数组进行排序，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.sort()` 根据给定属性对数组进行排序。
3. 使用 `String.prototype.localeCompare()` 比较给定属性的值。

以下是一个你可以使用的示例代码片段：

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

你可以使用对象数组和返回要排序属性的 getter 函数来调用 `alphabetical` 函数。以下是一个示例用法：

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
