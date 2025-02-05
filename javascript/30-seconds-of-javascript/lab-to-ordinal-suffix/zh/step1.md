# 将数字转换为序数后缀的函数

要将数字转换为序数后缀，请使用 `toOrdinalSuffix` 函数。

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 该函数接受一个数字作为输入，并将其作为带有正确序数指示后缀的字符串返回。
- 使用取模运算符（`%`）来找到个位数和十位数的值。
- 找出与哪种序数模式匹配的数字。
- 如果数字在十几（teens）模式中找到，则使用十几（teens）的序数。

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

以下是使用 `toOrdinalSuffix` 函数的示例：

```js
toOrdinalSuffix("123"); // '123rd'
```
