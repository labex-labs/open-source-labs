# 响应事件

> VM 中已提供 React 项目。一般来说，你只需在 `App.js` 中添加代码。

请使用以下命令安装依赖项：

```bash
npm i
```

React 允许你向 JSX 添加事件处理程序。事件处理程序是你自己的函数，会在诸如点击、悬停、聚焦表单输入等交互时触发。

要添加事件处理程序，你首先要定义一个函数，然后将其作为属性 [传递给适当的 JSX 标签](https://react.dev/learn/passing-props-to-a-component)。例如，这里有一个目前什么都不做的按钮：

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

你可以通过以下三个步骤让它在用户点击时显示一条消息：

1. 在 `Button` 组件内部声明一个名为 `handleClick` 的函数。
2. 在该函数内部实现逻辑（使用 `alert` 显示消息）。
3. 将 `onClick={handleClick}` 添加到 `<button>` JSX 中。

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

你定义了 `handleClick` 函数，然后将其作为属性传递给 `<button>`。`handleClick` 是一个事件处理程序。事件处理程序函数：

通常在组件内部定义。
名称以 `handle` 开头，后面跟着事件名称。

要运行该项目，请使用以下命令。然后，你可以刷新 **Web 8080** 标签页来预览网页。

```bash
npm start
```

按照惯例，事件处理程序通常命名为 `handle` 加上事件名称。你经常会看到 `onClick={handleClick}`、`onMouseEnter={handleMouseEnter}` 等等。

或者，你可以在 JSX 中内联定义事件处理程序：

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

或者，更简洁地，使用箭头函数：

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

所有这些样式都是等效的。内联事件处理程序对于短函数很方便。
