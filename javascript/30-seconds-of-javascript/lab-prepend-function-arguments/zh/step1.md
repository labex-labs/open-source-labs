# 使用偏应用前置函数参数

要开始练习编码，请打开终端/SSH 并输入 `node`。

函数 `partial` 用于创建一个新函数，该函数使用 `partials` 作为第一个参数来调用 `fn`。

- 使用展开运算符（`...`）将 `partials` 前置到 `fn` 的参数列表中。

```js
const partial =
  (fn, ...partials) =>
  (...args) =>
    fn(...partials, ...args);
```

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetHello = partial(greet, "Hello");
greetHello("John"); // 'Hello John!'
```
