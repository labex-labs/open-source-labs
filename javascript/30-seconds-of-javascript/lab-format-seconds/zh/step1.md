# 将秒数格式化为 ISO 时间的函数

要使用此代码，请打开终端/SSH 并输入 `node`。此函数以秒数作为参数，并返回 ISO 时间格式。其工作原理如下：

- 将秒数除以适当的值，以获取 `小时`、`分钟` 和 `秒` 的对应值。
- 将数字的符号存储在一个变量中，以便将其添加到结果的开头。
- 使用 `Array.prototype.map()` 结合 `Math.floor()` 和 `String.prototype.padStart()` 来将每个部分转换为字符串并进行格式化。
- 使用 `Array.prototype.join()` 将这些值组合成一个字符串。

以下是代码：

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

你可以使用以下示例测试该函数：

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
