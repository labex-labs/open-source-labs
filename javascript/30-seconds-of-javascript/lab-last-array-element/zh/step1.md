# 如何在JavaScript中获取数组的最后一个元素

要开始编码，请打开终端/SSH并输入 `node`。以下函数返回数组中的最后一个元素：

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

要使用它，你需要提供一个数组作为参数。该函数会检查数组是否为真值且具有 `length` 属性。如果这两个条件都为真，它会计算数组最后一个元素的索引并返回该元素。否则，它返回 `undefined`。

以下是一些示例：

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
