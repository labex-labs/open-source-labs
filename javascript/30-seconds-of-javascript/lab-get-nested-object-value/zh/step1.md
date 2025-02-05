# 如何从路径字符串中检索嵌套对象属性

要进行编码练习，请打开终端/SSH并输入 `node`。

以下函数通过使用路径字符串中指定的选择器从对象中检索一组属性。要实现这一点，请执行以下步骤：

1. 使用 `Array.prototype.map()` 遍历每个选择器，并应用 `String.prototype.replace()` 将方括号替换为点号。
2. 使用 `String.prototype.split()` 将每个选择器拆分为字符串数组。
3. 使用 `Array.prototype.filter()` 移除任何空值。
4. 使用 `Array.prototype.reduce()` 检索每个选择器指示的值。

以下是该函数：

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

你可以使用此函数通过路径字符串从嵌套对象中检索值。以下是一个示例：

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
