# 代码实践：从数组中获取随机元素

为了练习编码，请打开终端/SSH 并输入 `node`。以下代码利用 Fisher-Yates 算法对数组进行洗牌，并从数组中在唯一键处获取 `n` 个随机且唯一的元素，最多为数组的大小。

```js
const sampleSize = ([...arr], n = 1) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr.slice(0, n);
};
```

要使用此代码，请使用一个数组和一个可选的要获取的元素数量 `n` 调用 `sampleSize()`。如果未提供 `n`，则该函数将仅从数组中随机返回一个元素。

```js
sampleSize([1, 2, 3], 2); // [3, 1]
sampleSize([1, 2, 3], 4); // [2, 3, 1]
```
