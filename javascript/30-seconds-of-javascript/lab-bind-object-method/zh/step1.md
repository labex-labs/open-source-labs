# 绑定对象方法的函数

要创建一个将对象方法绑定到其上下文并可选择在前面添加其他参数的函数，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 定义一个接受三个参数的函数：对象上下文、方法键以及要在前面添加的任何其他参数。
3. 该函数应返回一个新函数，该新函数使用 `Function.prototype.apply()` 将方法绑定到对象上下文。
4. 使用展开运算符 (`...`) 将任何其他提供的参数添加到参数列表的前面。
5. 以下是一个示例实现：

```js
const bindKey =
  (context, fn, ...boundArgs) =>
  (...args) =>
    context[fn].apply(context, [...boundArgs, ...args]);
```

6. 要测试该函数，请创建一个带有方法的对象，并使用 `bindKey()` 对其进行绑定。然后，使用一些参数调用绑定的方法。

```js
const freddy = {
  user: "fred",
  greet: function (greeting, punctuation) {
    return greeting + " " + this.user + punctuation;
  }
};
const freddyBound = bindKey(freddy, "greet");
console.log(freddyBound("hi", "!")); // 'hi fred!'
```
