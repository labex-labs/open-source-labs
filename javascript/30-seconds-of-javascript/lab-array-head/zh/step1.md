# 如何在 JavaScript 中获取数组的第一个元素

要在 JavaScript 中获取数组的第一个元素，你可以使用 `head` 函数。以下是使用方法：

1. 打开终端/SSH。
2. 输入 `node` 开始练习编码。
3. 使用以下代码获取数组的头部元素：

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. 以数组作为参数调用 `head` 函数以获取第一个元素。如果数组为空或为假值，该函数将返回 `undefined`。

以下是一些示例：

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
