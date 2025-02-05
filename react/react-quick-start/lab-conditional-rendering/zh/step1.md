# 条件渲染

> VM 中已提供 React 项目。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

在 React 中，没有用于编写条件的特殊语法。相反，你将使用与编写常规 JavaScript 代码时相同的技术。例如，你可以使用 `if` 语句有条件地包含 JSX：

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

如果你更喜欢更紧凑的代码，可以使用条件 `?` 运算符。与 `if` 不同，它在 JSX 内部起作用：

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

当你不需要 else 分支时，也可以使用更短的逻辑 `&&` 语法：

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

如果 `isPacked` 属性为真，此代码将返回一个不同的 JSX 树。通过此更改，一些项目在末尾会有一个复选标记：

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页以预览网页。

```bash
npm start
```
