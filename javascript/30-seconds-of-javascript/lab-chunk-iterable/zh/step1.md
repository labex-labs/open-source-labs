# 将可迭代对象分块

要将一个可迭代对象分块为指定大小的较小数组，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 在给定的可迭代对象上使用 `for...of` 循环，使用 `Array.prototype.push()` 将每个新值添加到当前的 `块` 中。
3. 使用 `Array.prototype.length` 检查当前的 `块` 是否达到所需的 `大小`，如果达到则 `yield` 该值。
4. 使用 `Array.prototype.length` 检查最后一个 `块`，如果不为空则 `yield` 它。
5. 使用以下代码：

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. 使用此代码测试该函数：

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
