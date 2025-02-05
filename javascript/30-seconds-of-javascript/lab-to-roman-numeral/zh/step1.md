# 将整数转换为罗马数字

要将整数转换为其罗马数字表示形式，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。

2. 函数 `toRomanNumeral()` 接受 `1` 到 `3999` 之间（包括两端）的值。

3. 创建一个查找表，其中包含以（罗马数字值，整数）形式的双值数组。

4. 使用 `Array.prototype.reduce()` 遍历 `lookup` 中的值，并反复将 `num` 除以该值。

5. 使用 `String.prototype.repeat()` 将罗马数字表示形式添加到累加器中。

以下是 `toRomanNumeral()` 函数的代码：

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

你可以使用以下示例测试该函数：

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
