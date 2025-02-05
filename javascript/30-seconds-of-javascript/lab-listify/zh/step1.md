# 如何在 JavaScript 中将对象映射为数组

要在 JavaScript 中将对象映射为数组，可以使用 `listify()` 函数。具体做法如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。

2. 使用 `Object.entries()` 获取对象键值对的数组。

3. 使用 `Array.prototype.reduce()` 将数组映射为对象。

4. 使用 `mapFn` 映射对象的键和值，并使用 `Array.prototype.push()` 将映射后的值添加到数组中。

以下是 `listify()` 函数的代码：

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

以下是如何将其与名为 `people` 的对象一起使用的示例：

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

使用此函数，你可以轻松地在 JavaScript 中将对象映射为数组。
