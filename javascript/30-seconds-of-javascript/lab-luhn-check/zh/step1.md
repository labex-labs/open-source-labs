# Luhn 校验

要使用Luhn算法来验证识别号码，如信用卡号码、国际移动设备识别码（IMEI）、国家提供者识别码，请遵循以下步骤：

1. 打开终端/SSH并输入`node`以开始练习编码。
2. 结合使用以下方法：`String.prototype.split()`、`Array.prototype.reverse()`、`Array.prototype.map()`和`parseInt()`来获取一个数字数组。
3. 使用`Array.prototype.shift()`获取最后一位数字。
4. 使用`Array.prototype.reduce()`来实现Luhn算法。
5. 如果`sum`能被`10`整除，则返回`true`，否则返回`false`。

以下是代码：

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

你可以使用以下示例测试Luhn校验函数：

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
