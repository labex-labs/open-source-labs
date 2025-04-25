# 数字格式化函数

要使用本地数字格式顺序格式化数字，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Number.prototype.toLocaleString()` 方法将数字转换为使用本地数字格式分隔符。
3. 将你要格式化的数字作为参数传递给函数。

以下是一个示例实现：

```js
const formatNumber = (num) => num.toLocaleString();
```

以下是一些使用该函数的示例：

```js
formatNumber(123456); // 在 `en-US` 中为 '123,456'
formatNumber(15675436903); // 在 `de-DE` 中为 '15.675.436.903'
```
