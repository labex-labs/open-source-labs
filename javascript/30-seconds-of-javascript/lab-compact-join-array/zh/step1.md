# 以下是关于如何压缩并连接数组的提示

要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是如何从数组中移除虚假值并将其余值组合成一个字符串的方法：

- 使用 `Array.prototype.filter()` 过滤掉虚假值，如 `false`、`null`、`0`、`""`、`undefined` 和 `NaN`。
- 使用 `Array.prototype.join()` 将其余值连接成一个字符串。

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

然后调用该函数并传入一个数组作为参数：

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
