# 反转对象的函数

要在不改变原始对象的情况下反转对象的键值对，请使用 `invertKeyValues` 函数。

- 在终端/SSH 中输入 `invertKeyValues(obj, fn)` 来调用该函数，其中 `obj` 是要反转的对象，`fn` 是一个可选函数，将应用于反转后的键。

- `Object.keys()` 和 `Array.prototype.reduce()` 方法用于创建一个具有反转键值对的新对象，如果提供了函数，则将其应用于每个反转后的键。

- 如果省略 `fn`，则函数仅返回反转后的键，而不对其应用任何函数。

- 该函数返回一个对象，其中每个反转后的值都是负责生成该反转后值的键的数组。

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

示例用法：

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
