# 对数组元素进行分组

要根据数组元素在原始数组中的位置对其进行分组，请使用以下提供的 `zip` 函数。

- 打开终端/SSH 并输入 `node` 开始练习编码。
- `zip` 函数使用 `Math.max()` 和 `Function.prototype.apply()` 来获取参数中最长的数组。
- 它创建一个具有该长度的数组作为返回值，并使用 `Array.from()` 和一个映射函数来创建一个分组元素的数组。
- 如果参数数组的长度不同，则在找不到值的地方使用 `undefined`。

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

示例用法：

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
