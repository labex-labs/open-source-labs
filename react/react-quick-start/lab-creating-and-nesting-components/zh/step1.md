# 创建和嵌套组件

> 虚拟机中已提供 React 项目。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

React 应用由组件构成。组件是 UI（用户界面）的一部分，有自己的逻辑和外观。一个组件可以小到一个按钮，也可以大到一整个页面。

React 组件是返回标记的 JavaScript 函数：

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

既然你已经声明了 `MyButton`，就可以将它嵌套到另一个组件中：

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

注意 `<MyButton />` 以大写字母开头。通过这种方式你就知道它是一个 React 组件。React 组件名必须始终以大写字母开头，而 HTML 标签必须是小写的。

`export default` 关键字指定了文件中的主组件。如果你不熟悉某些 JavaScript 语法，[MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) 和 [javascript.info](https://javascript.info/import-export) 有很好的参考文档。

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页来预览网页。

```bash
npm start
```
