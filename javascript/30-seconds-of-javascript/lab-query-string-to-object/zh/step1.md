# 将查询字符串转换为对象

要将查询字符串或 URL 转换为对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.split()` 从给定的 `url` 中提取参数。
3. 使用 `URLSearchParams` 构造函数创建一个对象，并使用展开运算符 (`...`) 将其转换为键值对数组。
4. 使用 `Array.prototype.reduce()` 将键值对数组转换为对象。

以下是将查询字符串转换的代码：

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

示例用法：

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
