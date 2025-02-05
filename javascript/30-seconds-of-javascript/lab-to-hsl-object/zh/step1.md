# 将 HSL 转换为对象

要将 `hsl()` 颜色字符串转换为包含每种颜色数值的对象，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `String.prototype.match()` 获取一个包含数值的 3 个字符串的数组。
- 使用 `Array.prototype.map()` 结合 `Number` 将字符串转换为数值数组。
- 使用数组解构将值存储到命名变量中。
- 从命名变量创建一个合适的对象。

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

示例用法：

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
