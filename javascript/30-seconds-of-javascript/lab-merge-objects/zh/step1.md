# 对象合并函数

要合并两个或更多对象，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始编码。
2. 使用 `Array.prototype.reduce()` 以及 `Object.keys()` 遍历所有对象和键。
3. 使用 `Object.prototype.hasOwnProperty()` 和 `Array.prototype.concat()` 为多个对象中存在的键追加值。
4. 使用给定的代码片段通过组合两个或更多对象来创建一个新对象。

```js
const merge = (...objs) =>
  [...objs].reduce(
    (acc, obj) =>
      Object.keys(obj).reduce((a, k) => {
        acc[k] = acc.hasOwnProperty(k)
          ? [].concat(acc[k]).concat(obj[k])
          : obj[k];
        return acc;
      }, {}),
    {}
  );
```

例如，考虑以下对象：

```js
const object = {
  a: [{ x: 2 }, { y: 4 }],
  b: 1
};
const other = {
  a: { z: 3 },
  b: [2, 3],
  c: "foo"
};
```

当你使用 `merge()` 函数合并这两个对象时，会得到以下结果：

```js
merge(object, other);
// { a: [ { x: 2 }, { y: 4 }, { z: 3 } ], b: [ 1, 2, 3 ], c: 'foo' }
```
