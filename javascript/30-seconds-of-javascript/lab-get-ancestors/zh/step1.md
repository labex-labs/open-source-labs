# 检索元素的祖先元素

要从文档根节点到指定元素检索该元素的祖先元素，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Node.parentNode` 和 `while` 循环向上遍历元素的祖先树。
3. 使用 `Array.prototype.unshift()` 将每个新的祖先元素添加到数组的开头。

以下是实现上述步骤的示例代码：

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

要检索特定元素的祖先元素，请使用 `querySelector()` 方法选择该元素，并将其作为参数传递给 `getAncestors()` 函数。例如：

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

这将返回指定元素的所有祖先元素组成的数组，顺序是从文档根节点到该元素本身。
