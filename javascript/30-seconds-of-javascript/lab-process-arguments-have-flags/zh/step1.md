# 检查进程参数是否包含标志

要检查当前进程的参数是否包含指定的标志，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.every()` 和 `Array.prototype.includes()` 检查 `process.argv` 是否包含所有指定的标志。
3. 使用正则表达式测试指定的标志是否以 `-` 或 `--` 为前缀，并相应地添加前缀。

以下是一个展示如何实现此功能的代码片段：

```js
const hasFlags = (...flags) =>
  flags.every((flag) =>
    process.argv.includes(/^-{1,2}/.test(flag) ? flag : "--" + flag)
  );
```

你可以使用不同的标志来测试这个函数，如下所示：

```js
// node myScript.js -s --test --cool=true
hasFlags("-s"); // true
hasFlags("--test", "cool=true", "-s"); // true
hasFlags("special"); // false
```
