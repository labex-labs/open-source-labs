# 如何在 JavaScript 中从数组中提取值

要在 JavaScript 中从数组中提取特定值，可以使用`Array.prototype.filter()`和`Array.prototype.includes()`方法。以下是具体做法：

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

`pull`函数接受一个数组以及一个或多个表示要移除的值的参数。然后，该函数通过使用`Array.prototype.filter()`过滤掉指定的值来创建一个新数组。接着，它通过将原始数组的长度重置为`0`并仅使用`Array.prototype.push()`将提取的值重新填充到原始数组中，从而改变原始数组。

以下是如何使用`pull`函数的示例：

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

在这个示例中，`pull`函数从`myArray`数组中移除了所有出现的`'a'`和`'c'`，并返回一个只包含值`'b'`和`'b'`的新数组。
