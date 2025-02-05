# 用于追加参数的函数

要创建一个将参数追加到其接收的参数列表中的函数，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始编码练习。
2. 使用展开运算符 (`...`) 将 `partials` 追加到 `fn` 的参数列表中。
3. 使用以下代码创建函数：

```js
const partialRight =
  (fn, ...partials) =>
  (...args) =>
    fn(...args, ...partials);
```

4. 使用一个示例测试该函数，例如：

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetJohn = partialRight(greet, "John");
greetJohn("Hello"); // 'Hello John!'
```
