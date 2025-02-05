# 可折叠内容

> VM 中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

此函数会渲染一个可折叠组件，该组件带有一个用于切换其内容可见性的按钮。以下是使用方法：

1. 使用 `useState()` 钩子创建 `isCollapsed` 状态变量，它表示内容当前是折叠还是展开。将其初始化为 `collapsed`。
2. 使用 `<button>` 元素切换 `isCollapsed` 状态，并显示/隐藏通过 `children` 属性传递下来的内容。
3. 使用 `isCollapsed` 为内容容器应用适当的 CSS 类，即 `collapsed` 或 `expanded`，这决定了它的外观。
4. 根据 `isCollapsed` 状态更新内容容器的 `aria-expanded` 属性，以使该组件对残疾用户也可访问。

以下是此组件所需的 CSS 代码：

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

以下是 JavaScript 代码：

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "显示" : "隐藏"} 内容
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

要使用此组件，只需将你想要折叠的内容作为参数调用它：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>这是一个可折叠内容</h1>
    <p>你好，世界！</p>
  </Collapse>
);
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
