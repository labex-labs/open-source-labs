# 使用给定上下文创建函数

要使用给定上下文创建函数，请使用 `bind` 函数。首先，打开终端/SSH 并输入 `node`。

`bind` 函数创建一个新函数，该函数使用给定上下文调用原始函数。它还可以选择将任何额外提供的参数添加到参数列表的开头。

要使用 `bind`，传入原始函数（`fn`）和所需的上下文（`context`）。你还可以传入任何应绑定到函数的额外参数（`...boundArgs`）。

`bind` 函数返回一个新函数，该函数使用 `Function.prototype.apply()` 将给定的 `context` 应用于 `fn`。它还使用展开运算符（`...`）将任何额外提供的参数添加到参数列表的开头。

以下是 `bind` 的一个示例用法：

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

在这个示例中，我们定义了一个 `greet` 函数，它接受两个参数（`greeting` 和 `punctuation`），并返回一个字符串，该字符串将 `greeting`、当前上下文（`this`）的 `user` 属性和 `punctuation` 连接起来。

然后，我们创建一个新对象（`freddy`），其 `user` 属性设置为 `'fred'`。

最后，我们使用 `bind` 创建一个新函数（`freddyBound`），传入 `greet` 函数和 `freddy` 对象作为所需的上下文。然后，我们可以使用两个额外的参数（`'hi'` 和 `'!'`）调用 `freddyBound`，这些参数会与绑定的 `freddy` 上下文一起传递给原始的 `greet` 函数。结果输出为 `'hi fred!'`。
