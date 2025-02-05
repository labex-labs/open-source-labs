# 如何获取整数的上午/下午后缀

要开始编码，请打开终端/SSH并输入`node`。

以下是一个将整数转换为带有上午/下午后缀的12小时制格式字符串的函数。

为此，请使用取模运算符（`%`）和条件检查。

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

以下是一些如何使用此函数的示例：

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

此函数接受一个整数作为参数，并返回一个带有上午/下午后缀的字符串。
