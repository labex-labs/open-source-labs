# 将生成器输出转换为数组

要将生成器函数的输出转换为数组，请使用展开运算符（`...`）。要开始练习编码，请打开终端/SSH 并输入 `node`。

以下是一个将生成器转换为数组的示例函数：

```js
const generatorToArray = (gen) => [...gen];
```

你可以按如下方式使用此函数：

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
