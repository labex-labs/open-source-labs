# 根据条件和键过滤对象

要根据条件过滤对象数组，同时过滤掉未指定的键，请使用 `reducedFilter()` 函数。

以下是具体步骤：

1. 使用 `Array.prototype.filter()` 根据谓词 `fn` 过滤数组，以便返回条件返回真值的对象。

2. 对过滤后的数组使用 `Array.prototype.map()` 以返回新对象。

3. 使用 `Array.prototype.reduce()` 过滤掉未作为 `keys` 参数提供的键。

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

以下是 `reducedFilter()` 函数的一个示例用法：

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// 输出: [{ id: 2, name:'mike'}]
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
