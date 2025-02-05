# 如何使用 JavaScript 计算字符串中的子串

如果你想练习编码，打开终端/SSH 并输入 `node`。这个 JavaScript 函数用于计算给定字符串中指定子串的出现次数。

要使用此函数，请执行以下步骤：

1. 声明一个名为 `countSubstrings` 的函数，该函数接受两个参数：`str` 和 `searchValue`。
2. 初始化两个变量：`count` 和 `i`。
3. 使用 `Array.prototype.indexOf()` 方法在 `str` 中搜索 `searchValue`。
4. 如果找到该值，则增加 `count` 变量并更新 `i` 变量。
5. 使用 `while` 循环，一旦 `Array.prototype.indexOf()` 返回的值为 `-1` 就返回。
6. 返回 `count` 变量。

这是 `countSubstrings` 函数的代码：

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

你可以使用以下示例测试该函数：

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
