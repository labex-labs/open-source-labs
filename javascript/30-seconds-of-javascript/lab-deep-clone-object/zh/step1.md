# 对象深度克隆的操作指南

要深度克隆一个对象，请按以下步骤操作：

1. 创建一个新的终端/SSH实例，输入`node`以开始练习编码。
2. 使用递归来克隆原始值、数组和对象，但不包括类实例。
3. 检查传入的对象是否为`null`，如果是，则返回`null`。
4. 使用`Object.assign()`和一个空对象（`{}`）来创建原始对象的浅克隆。
5. 使用`Object.keys()`和`Array.prototype.forEach()`来确定哪些键值对需要深度克隆。
6. 如果对象是一个`Array`，将克隆对象的`length`设置为原始数组的长度，并使用`Array.from()`来创建克隆。
7. 使用以下代码实现深度克隆：

```js
const deepClone = (obj) => {
  if (obj === null) return null;
  let clone = Object.assign({}, obj);
  Object.keys(clone).forEach(
    (key) =>
      (clone[key] =
        typeof obj[key] === "object" ? deepClone(obj[key]) : obj[key])
  );
  if (Array.isArray(obj)) {
    clone.length = obj.length;
    return Array.from(clone);
  }
  return clone;
};
```

使用以下代码测试你的深度克隆函数：

```js
const a = { foo: "bar", obj: { a: 1, b: 2 } };
const b = deepClone(a); // a!== b, a.obj!== b.obj
```
