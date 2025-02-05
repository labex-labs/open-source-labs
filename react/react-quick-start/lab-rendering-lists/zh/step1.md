# 渲染列表

> 实验项目已在虚拟机中提供。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

你将依赖于诸如 for 循环和数组 `map()` 函数等 JavaScript 特性来渲染组件列表。

例如，假设你有一个产品数组：

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

在你的组件内部，使用 `map()` 函数将产品数组转换为 `<li>` 项的数组：

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

注意 `<li>` 是如何具有一个 `key` 属性的。对于列表中的每个项，你应该传递一个字符串或数字，它在其同级项中唯一标识该项。通常，一个键应该来自你的数据，比如数据库 ID。如果稍后你插入、删除或重新排序这些项，React 使用你的键来了解发生了什么。

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页来预览网页。

```bash
npm start
```
