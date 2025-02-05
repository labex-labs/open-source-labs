# 如何在 JavaScript 中重新排列函数参数

要在 JavaScript 中重新排列函数参数，你可以使用 `rearg()` 函数。首先，创建一个函数，该函数使用根据指定索引排列的参数来调用提供的函数。你可以使用 `Array.prototype.map()` 根据 `indexes` 对参数重新排序。然后，使用展开运算符 (`...`) 将转换后的参数传递给 `fn`。

以下是使用 `rearg()` 函数的示例：

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

在此示例中，我们使用 `rearg()` 创建一个新函数，该函数会重新排列另一个函数的参数。

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

在上述代码中，我们创建了一个新函数 `rearged`，它会重新排列函数 `function(a, b, c) { return [a, b, c]; }` 的参数。`indexes` 参数指定了参数应重新排列的顺序。在这种情况下，我们希望第三个参数排在第一位，第一个参数排在第二位，第二个参数排在第三位。当我们调用 `rearged('b', 'c', 'a')` 时，它会返回 `['a', 'b', 'c']`，这是使用重新排列后的参数调用原始函数的结果。
