# 使用 `flip` 重新排序函数参数

要交换函数参数的顺序，可以使用 `flip` 函数。这个函数接受一个函数作为参数，并返回一个新函数，该新函数会交换第一个和最后一个参数。

要实现 `flip`：

- 使用参数解构和带有可变参数的闭包。
- 使用展开运算符 (`...`) 拼接第一个参数，使其在应用其余参数之前成为最后一个参数。

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

以下是一个如何使用 `flip` 重新排序 `Object.assign` 参数的示例：

```js
let a = { name: "John Smith" };
let b = {};

// 创建一个新函数，用于交换 Object.assign 的参数
const mergeFrom = flip(Object.assign);

// 创建一个新函数，将第一个参数绑定到 a
let mergePerson = mergeFrom.bind(null, a);

// 使用 b 作为第二个参数调用新函数
mergePerson(b); // 此时 b 等于 a

// 或者，不使用新函数直接合并 a 和 b
b = {};
Object.assign(b, a); // 此时 b 等于 a
```
