# 如何在 JavaScript 中从数组末尾移除元素

要在 JavaScript 中从数组末尾移除元素，可以使用 `Array.prototype.slice()` 方法。具体做法如下：

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

此函数会创建一个新数组，其中包含原始数组的最后 `n` 个元素。使用方法如下：

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

要使用此函数，请打开终端/SSH 并输入 `node` 开始练习编码。
