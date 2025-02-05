# 如何在JavaScript中扁平化对象

要在JavaScript中使用带键路径的对象来实现扁平化，可按以下步骤操作：

1. 打开终端/SSH并输入 `node` 以开始练习编码。

2. 使用嵌套的 `Array.prototype.reduce()` 将扁平路径转换为叶节点。

3. 使用 `String.prototype.split()` 以点号作为分隔符拆分每个键，并使用 `Array.prototype.reduce()` 根据这些键添加对象。

4. 如果当前累加器已经包含针对某个特定键的值，则返回其值作为下一个累加器。

5. 否则，将适当的键值对添加到累加器对象中，并返回该值作为累加器。

以下是 `unflattenObject` 函数的代码：

```js
const unflattenObject = (obj) =>
  Object.keys(obj).reduce((res, k) => {
    k.split(".").reduce(
      (acc, e, i, keys) =>
        acc[e] ||
        (acc[e] = isNaN(Number(keys[i + 1]))
          ? keys.length - 1 === i
            ? obj[k]
            : {}
          : []),
      res
    );
    return res;
  }, {});
```

你可以使用 `unflattenObject` 函数在JavaScript中扁平化对象：

```js
unflattenObject({ "a.b.c": 1, d: 1 }); // { a: { b: { c: 1 } }, d: 1 }
unflattenObject({ "a.b": 1, "a.c": 2, d: 3 }); // { a: { b: 1, c: 2 }, d: 3 }
unflattenObject({ "a.b.0": 8, d: 3 }); // { a: { b: [ 8 ] }, d: 3 }
```
