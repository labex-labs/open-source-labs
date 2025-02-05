# 数组洗牌算法

要在JavaScript中对数组进行洗牌操作，请使用费雪-耶茨（Fisher-Yates）算法。该算法会随机重新排列数组中的元素，并返回一个新数组。

要开始练习编码，请打开终端/SSH并输入 `node`。

以下是费雪-耶茨算法的代码：

```js
const shuffle = ([...arr]) => {
  let m = arr.length;
  while (m) {
    const i = Math.floor(Math.random() * m--);
    [arr[m], arr[i]] = [arr[i], arr[m]];
  }
  return arr;
};
```

要对数组进行洗牌操作，将数组传递给 `shuffle` 函数，它将返回洗牌后的数组。例如：

```js
const foo = [1, 2, 3];
shuffle(foo); // 返回 [2, 3, 1]，而 foo 仍然是 [1, 2, 3]
```
