# 计算值频率的说明

要计算数组中值的频率，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()` 方法将唯一值映射到对象的键，并在每次遇到相同值时将其添加到现有键中。这将创建一个以数组的唯一值作为键，以它们的频率作为值的对象。
3. 此操作的代码如下：

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4. 要使用此函数，请将数组作为参数调用 `frequencies`。例如：

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

按照这些说明，你可以轻松计算任何给定数组中值的频率。
