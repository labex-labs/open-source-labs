# 克隆正则表达式

要克隆正则表达式，请使用 `RegExp` 构造函数、`RegExp.prototype.source` 和 `RegExp.prototype.flags`。

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

这段代码将创建给定正则表达式的克隆。例如：

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp 与 regExp2 不相等
```
