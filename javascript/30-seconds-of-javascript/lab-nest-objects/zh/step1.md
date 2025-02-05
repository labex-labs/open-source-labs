# 如何在 JavaScript 中使用递归嵌套对象

要在扁平数组中递归地嵌套对象，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用递归嵌套相互链接的对象。
3. 使用 `Array.prototype.filter()` 过滤出 `id` 与 `link` 匹配的项。
4. 使用 `Array.prototype.map()` 将每个项映射到一个新对象，该对象具有一个 `children` 属性，该属性会根据哪些项是当前项的子项来递归地嵌套这些项。
5. 省略第二个参数 `id`，默认为 `null`，这表示该对象未链接到另一个对象（即它是顶级对象）。
6. 省略第三个参数 `link`，使用 `'parent_id'` 作为默认属性，通过其 `id` 将对象链接到另一个对象。

以下是代码：

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

要使用 `nest()` 函数，请创建一个包含 `id` 属性和将它们链接到另一个对象的 `parent_id` 属性的对象数组。然后，调用 `nest()` 函数并将该数组作为参数传递。该函数将返回一个基于其 `parent_id` 属性进行嵌套的新对象数组。

例如：

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
