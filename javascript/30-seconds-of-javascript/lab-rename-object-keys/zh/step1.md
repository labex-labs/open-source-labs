# 如何在 JavaScript 中重命名对象的键

要根据提供的值重命名多个对象键，可以使用 `renameKeys` 函数。你需要遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 结合使用 `Object.keys()`、`Array.prototype.reduce()` 和展开运算符 (`...`) 来获取对象的键，并根据 `keysMap` 对其进行重命名。
3. 将 `keysMap` 和对象 (`obj`) 作为参数传递给 `renameKeys` 函数。
4. `renameKeys` 函数返回一个具有重命名键的新对象。

以下是使用 `renameKeys` 函数的示例：

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
