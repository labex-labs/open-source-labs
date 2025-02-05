# 在终端/SSH 中生成随机十六进制颜色代码

要在终端/SSH 中生成随机十六进制颜色代码，请按照以下步骤操作：

1. 打开终端/SSH。
2. 输入 `node`。
3. 使用以下代码生成一个随机的 24 位（6 \* 4 位）十六进制数：

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. 要生成随机十六进制颜色代码，调用函数 `randomHexColorCode()`。

示例：

```js
randomHexColorCode(); // '#e34155'
```

这将生成一个可在你的编码项目中使用的随机十六进制颜色代码。
