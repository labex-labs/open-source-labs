# 冒泡排序算法

要进行编码练习，请打开终端/SSH 并输入 `node` 以开始。冒泡排序算法用于对数字数组进行排序。

使用冒泡排序算法对数组进行排序的步骤：

1. 声明一个变量 `swapped`，用于指示在当前迭代期间是否有任何值被交换。

2. 使用展开运算符 (`...`) 克隆原始数组 `arr`。

3. 使用 `for` 循环遍历克隆数组的元素，在最后一个元素之前终止。

4. 使用嵌套的 `for` 循环遍历数组中从 `0` 到 `i` 的部分，交换任何相邻的无序元素，并将 `swapped` 设置为 `true`。

5. 如果在一次迭代后 `swapped` 为 `false`，则无需再进行更改，因此返回克隆数组。

示例代码：

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
