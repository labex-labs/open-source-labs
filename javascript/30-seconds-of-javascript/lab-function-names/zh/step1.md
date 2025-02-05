# 如何在 JavaScript 中从对象获取函数属性名称

要从对象获取函数属性名称的数组，请使用下面提供的 `functions` 函数。此函数还可以选择包含继承的属性。

以下是使用 `functions` 函数的方法：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Object.keys()` 遍历对象自身的属性。
3. 如果你想包含继承的属性，将 `inherited` 参数设置为 `true`，并使用 `Object.getPrototypeOf()` 获取对象的继承属性。
4. 使用 `Array.prototype.filter()` 只保留那些是函数的属性。
5. 省略第二个参数 `inherited`，默认情况下不包含继承的属性。

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

以下是 `functions` 函数的一个示例用法：

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
