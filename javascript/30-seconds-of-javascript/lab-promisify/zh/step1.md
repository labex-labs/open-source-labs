# 将异步函数转换为返回 Promise 的函数

要将异步函数转换为返回 Promise，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用柯里化返回一个返回 `Promise` 的函数，该 `Promise` 调用原始函数。
3. 使用剩余参数运算符 (`...`) 传入所有参数。
4. 如果你使用的是 Node 8+，可以使用[`util.promisify`](https://nodejs.org/api/util.html#util_util_promisify_original)。
5. 以下是一个代码片段示例：

```js
const promisify =
  (func) =>
  (...args) =>
    new Promise((resolve, reject) =>
      func(...args, (err, result) => (err ? reject(err) : resolve(result)))
    );
```

6. 要使用此函数，定义异步函数并将其作为参数传递给 `promisify` 函数。返回的函数现在将返回一个 Promise。

```js
const delay = promisify((d, cb) => setTimeout(cb, d));
delay(2000).then(() => console.log("Hi!")); // Promise 在 2 秒后 resolve
```

`delay` 函数是一个异步函数的示例，它现在使用 `promisify` 函数返回一个 Promise。
