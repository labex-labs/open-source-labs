# 如何在 Node.js 中将波浪线路径转换为绝对路径

要在 Node.js 中开始编码实践，请打开终端或 SSH 并输入 `node`。要将波浪线路径转换为绝对路径，请使用以下代码：

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

这段代码使用了 `String.prototype.replace()` 方法和一个正则表达式，以及 `os.homedir()` 函数，将路径开头的 `~` 替换为用户主目录。以下是使用 `untildify` 函数的示例：

```js
untildify("~/node"); // 返回 '/Users/aUser/node'
```
