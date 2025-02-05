# 如何将数组连接成字符串

要将数组的所有元素连接成一个字符串，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `join()` 函数，并传入以下参数：
   - `arr`：要连接的数组。
   - `separator`（可选）：数组元素之间使用的分隔符。如果未指定，将使用默认分隔符 `,`。
   - `end`（可选）：数组最后两个元素之间使用的分隔符。如果未指定，默认将使用与 `separator` 相同的值。
3. `join()` 函数使用 `Array.prototype.reduce()` 将数组的元素组合成一个字符串。
4. 返回最终的字符串。

以下是 `join()` 函数的代码：

```js
const join = (arr, separator = ",", end = separator) =>
  arr.reduce(
    (acc, val, i) =>
      i === arr.length - 2
        ? acc + val + end
        : i === arr.length - 1
          ? acc + val
          : acc + val + separator,
    ""
  );
```

以下是一些使用 `join()` 函数的示例：

```js
join(["pen", "pineapple", "apple", "pen"], ",", "&"); // 'pen,pineapple,apple&pen'
join(["pen", "pineapple", "apple", "pen"], ","); // 'pen,pineapple,apple,pen'
join(["pen", "pineapple", "apple", "pen"]); // 'pen,pineapple,apple,pen'
```
