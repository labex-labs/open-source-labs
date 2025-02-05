# 如何根据给定函数从数组中提取值

要开始练习编码，请打开终端/SSH 并输入 `node`。

`pullBy` 函数会根据给定的迭代函数过滤掉指定的值，从而改变原始数组。其工作原理如下：

1. 检查提供的最后一个参数是否为函数。
2. 使用 `Array.prototype.map()` 将迭代函数 `fn` 应用于所有数组元素。
3. 使用 `Array.prototype.filter()` 和 `Array.prototype.includes()` 提取不需要的值。
4. 设置 `Array.prototype.length` 将传入数组的长度重置为 `0`。
5. 使用 `Array.prototype.push()` 仅用提取的值重新填充数组。

以下是代码：

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

以下是使用它的示例：

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

请注意，在这个示例中，我们提取了所有 `x` 属性为 `1` 或 `3` 的元素。最终的 `myArray` 将只包含 `x` 属性为 `2` 的元素。
