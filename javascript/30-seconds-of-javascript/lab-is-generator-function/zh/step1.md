# 检查一个值是否为生成器函数

要检查一个值是否为生成器函数，你可以使用 `isGeneratorFunction` 函数。要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是 `isGeneratorFunction` 函数的工作原理：

- 它通过使用 `Object.prototype.toString()` 和 `Function.prototype.call()` 来检查给定的参数是否为生成器函数。
- 如果检查结果是 `'[object GeneratorFunction]'`，那么该值就是一个生成器函数。

以下是 `isGeneratorFunction` 函数的代码：

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

以下是一些使用它的示例：

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
