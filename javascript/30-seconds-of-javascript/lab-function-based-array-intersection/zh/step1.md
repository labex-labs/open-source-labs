# 如何使用 JavaScript 根据函数查找数组交集

要根据提供的比较函数找出两个数组中都存在的元素，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。

2. 结合使用 `Array.prototype.filter()` 和 `Array.prototype.findIndex()` 以及提供的比较函数来确定相交值。

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. 将两个数组和比较函数作为参数调用 `intersectionWith()` 函数。

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

这将根据提供的比较函数返回一个包含两个数组中相交值的数组。
