# 函数

> VM 中已提供 `index.html`。

[函数](https://developer.mozilla.org/en-US/docs/Glossary/Function) 是一种用于封装你希望复用的功能的方式。可以将一段代码定义为一个函数，当你在代码中调用该函数名时，它就会执行。这是避免重复编写相同代码的一个好方法。你已经见过函数的一些用法了。

例如：

```js
let myVariable = document.querySelector("h1");
```

```js
alert("你好！");
```

这些函数，`document.querySelector` 和 `alert`，是浏览器内置的。

> 请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。

如果你看到某个看起来像变量名，但后面跟着括号 `()` 的东西，那很可能是一个函数。函数通常接受 [参数](https://developer.mozilla.org/en-US/docs/Glossary/Argument)：它们执行任务所需的一些数据。参数放在括号内，如果有多个参数，则用逗号分隔。

例如，`alert()` 函数会在浏览器窗口中弹出一个对话框，但我们需要给它一个字符串作为参数，以告诉函数要显示什么消息。

你也可以定义自己的函数。

在下面的示例中，我们创建了一个简单的函数，它接受两个数字作为参数并将它们相乘：

> 打开终端/SSH 并输入 `node` 开始练习编码。

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

尝试在控制台中运行此函数；然后用几个参数进行测试。例如：

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **注意**：[`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return) 语句告诉浏览器将 `result` 变量从函数中返回，这样它就可以被使用了。这是必要的，因为在函数内部定义的变量仅在这些函数内部可用。这称为变量作用域。（阅读更多关于 [变量作用域](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope) 的内容。）
