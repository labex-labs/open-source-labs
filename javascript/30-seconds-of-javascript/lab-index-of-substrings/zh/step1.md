# 子字符串的索引

要在给定字符串中找到子字符串的所有索引，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用内置方法 `Array.prototype.indexOf()` 在 `str` 中搜索 `searchValue`。
3. 如果找到该值，则使用 `yield` 返回索引并更新索引 `i`。
4. 使用 `while` 循环，一旦 `Array.prototype.indexOf()` 返回的值为 `-1`，就终止生成器。

以下是实现上述步骤的示例代码：

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

你可以使用以下代码测试该函数：

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
