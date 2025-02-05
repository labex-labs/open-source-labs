# 使用 JSX 编写标记

> 实验项目已在虚拟机中提供。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

你上面看到的标记语法称为 JSX。它是可选的，但大多数 React 项目因其便利性而使用 JSX。

JSX 比 HTML 更严格。你必须关闭标签，如 `<br />`。你的组件也不能返回多个 JSX 标签。你必须将它们包装在一个共享的父标签中，比如 `<h1>...</h1>` 或一个空的 `<>...</>` 包装器：

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

如果你有很多 HTML 要转换为 JSX，可以使用 [在线转换器](https://transform.tools/html-to-jsx)。

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页来预览网页。

```bash
npm start
```
