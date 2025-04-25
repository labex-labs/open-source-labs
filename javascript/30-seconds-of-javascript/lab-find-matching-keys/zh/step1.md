# 查找匹配的键

要在对象中找到所有与给定值匹配的键，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.keys()` 获取对象的所有属性。
3. 使用 `Array.prototype.filter()` 测试每个键值对，并返回所有等于给定值的键。

以下是一个实现此逻辑的示例函数：

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

你可以像这样使用此函数：

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
