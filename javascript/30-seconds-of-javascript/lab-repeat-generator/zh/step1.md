# 使用重复生成器进行代码练习

为了练习编码，打开终端/SSH 并输入 `node` 来创建一个无限重复给定值的生成器。使用一个不终止的 `while` 循环，每次调用 `Generator.prototype.next()` 时都会 `yield` 一个值。然后，如果传递的值不是 `undefined`，则使用 `yield` 语句的返回值来更新返回值。

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

要测试生成器，使用值 `5` 创建一个实例，并调用 `repeater.next()` 以获取序列中的下一个值。输出将是 `{ value: 5, done: false }`。再次调用 `repeater.next()` 将返回相同的值。要更改值，调用 `repeater.next(4)`，它将返回 `{ value: 4, done: false }`。最后，调用 `repeater.next()` 将返回更新后的值 `{ value: 4, done: false }`。
