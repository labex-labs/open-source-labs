# 如何在 JavaScript 中延迟函数执行

要在 JavaScript 中延迟函数的执行，可以使用 `setTimeout()` 方法。具体做法如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用以下语法将函数 `fn` 的执行延迟 `ms` 毫秒：

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. 要将参数传递给函数，可像这样使用展开 (`...`) 运算符：

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "later"
); // 一秒后输出 'later'。
```

通过这段代码，所提供的函数 `fn` 将在指定的毫秒数 (`ms`) 之后被调用。`...args` 参数允许你向函数传递任意数量的参数。
