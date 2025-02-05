# 数组分区算法

要对数组进行分区，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 将提供的函数 `fn` 应用于给定数组 `arr` 中的每个值。
3. 每当 `fn` 返回一个新值时，拆分数组。
4. 使用 `Array.prototype.reduce()` 创建一个累加器对象，该对象保存结果数组以及从 `fn` 返回的最后一个值。
5. 使用 `Array.prototype.push()` 将 `arr` 中的每个值添加到累加器数组中的适当分区。
6. 返回结果数组。

以下是代码实现：

```js
const partitionBy = (arr, fn) =>
  arr.reduce(
    ({ res, last }, v, i, a) => {
      const next = fn(v, i, a);
      if (next !== last) res.push([v]);
      else res[res.length - 1].push(v);
      return { res, last: next };
    },
    { res: [] }
  ).res;
```

示例用法：

```js
const numbers = [1, 1, 3, 3, 4, 5, 5, 5];
partitionBy(numbers, (n) => n % 2 === 0); // [[1, 1, 3, 3], [4], [5, 5, 5]]
partitionBy(numbers, (n) => n); // [[1, 1], [3, 3], [4], [5, 5, 5]]
```
