# 线性搜索算法

为了练习编码，打开终端或 SSH 并输入 `node`。线性搜索算法用于在数组中找到给定元素的第一个索引。

它的工作原理如下：

- 使用 `for...in` 循环遍历给定数组的索引。
- 检查对应索引处的元素是否等于 `item`。
- 如果找到该元素，则返回索引。使用一元 `+` 运算符将其从字符串转换为数字。
- 如果在遍历整个数组后仍未找到该元素，则返回 `-1`。

以下是代码：

```js
const linearSearch = (arr, item) => {
  for (const i in arr) {
    if (arr[i] === item) return +i;
  }
  return -1;
};
```

要测试该函数，请使用数组和要搜索的值调用它：

```js
linearSearch([2, 9, 9], 9); // 1
linearSearch([2, 9, 9], 7); // -1
```
