# 过滤数组值

要根据谓词函数过滤数组，并仅返回谓词函数返回 `false` 的值，请执行以下步骤：

1. 将 `Array.prototype.filter()` 与谓词函数 `pred` 结合使用。
2. 过滤方法将只返回谓词函数返回 `false` 的值。
3. 要排除不匹配的值，将谓词函数和数组传递给 `reject()` 函数。

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

以下是一些如何使用 `reject()` 函数的示例：

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

通过遵循这些步骤，你可以轻松地根据谓词函数过滤数组并排除不匹配的值。
