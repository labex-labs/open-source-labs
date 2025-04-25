# 包含 URL 参数的对象

要创建一个包含当前 URL 参数的对象，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 将 `String.prototype.match()` 与适当的正则表达式一起使用，以提取所有键值对。
3. 使用 `Array.prototype.reduce()` 将它们映射并组合成一个对象。
4. 将 `location.search` 作为参数传递，以应用于当前 URL。

以下是代码：

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)), a
    ),
    {}
  );
```

你可以将此函数与任何 URL 一起使用，以获取包含其参数的对象。以下是一些示例：

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
