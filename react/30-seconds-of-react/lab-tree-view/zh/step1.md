# 可展开的对象树视图

> 虚拟机中已经提供了 `index.html` 和 `script.js`。一般来说，你只需要在 `script.js` 和 `style.css` 中添加代码。

以下代码呈现了一个 JSON 对象或数组的可折叠树视图。通过使用 `useState()` 钩子创建 `isToggled` 状态变量，你可以通过传递 `toggled` 属性来确定内容的初始状态（折叠/展开）。组件的外观是根据 `isParentToggled`、`isToggled`、`name` 以及对 `data` 进行 `Array.isArray()` 检查来确定的。

对于 `data` 中的每个子项，确定它是对象还是数组，并递归地呈现一个子树或具有适当样式的文本元素。要切换组件状态，呈现一个 `<span>` 元素，并将其 `onClick` 事件绑定到改变组件的 `isToggled` 状态。

CSS 样式是为组件的外观定义的，包括 `margin`、`position`、`border` 和 `display` 属性。

```jsx
const TreeView = ({
  data,
  toggled = true,
  name = null,
  isLast = true,
  isChildElement = false,
  isParentToggled = true
}) => {
  const [isToggled, setIsToggled] = React.useState(toggled);
  const isDataArray = Array.isArray(data);

  return (
    <div
      className={`tree-element ${isParentToggled && "collapsed"} ${
        isChildElement && "is-child"
      }`}
    >
      <span
        className={isToggled ? "toggler" : "toggler closed"}
        onClick={() => setIsToggled(!isToggled)}
      />
      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
      {isDataArray ? "[" : "{"}
      {!isToggled && "..."}
      {Object.keys(data).map((v, i, a) =>
        typeof data[v] === "object" ? (
          <TreeView
            key={`${name}-${v}-${i}`}
            data={data[v]}
            isLast={i === a.length - 1}
            name={isDataArray ? null : v}
            isChildElement
            isParentToggled={isParentToggled && isToggled}
          />
        ) : (
          <p
            key={`${name}-${v}-${i}`}
            className={isToggled ? "tree-element" : "tree-element collapsed"}
          >
            {isDataArray ? "" : <strong>{v}: </strong>}
            {data[v]}
            {i === a.length - 1 ? "" : ","}
          </p>
        )
      )}
      {isDataArray ? "]" : "}"}
      {!isLast ? "," : ""}
    </div>
  );
};
```

```css
.tree-element {
  margin: 0 0 0 4px;
  position: relative;
}

.tree-element.is-child {
  margin-left: 16px;
}

div.tree-element::before {
  content: "";
  position: absolute;
  top: 24px;
  left: 1px;
  height: calc(100% - 48px);
  border-left: 1px solid gray;
}

p.tree-element {
  margin-left: 16px;
}

.toggler {
  position: absolute;
  top: 10px;
  left: 0px;
  width: 0;
  height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 5px solid gray;
  cursor: pointer;
}

.toggler.closed {
  transform: rotate(90deg);
}

.collapsed {
  display: none;
}
```

```jsx
const data = {
  lorem: {
    ipsum: "dolor sit",
    amet: {
      consectetur: "adipiscing",
      elit: [
        "duis",
        "vitae",
        {
          semper: "orci"
        },
        {
          est: "sed ornare"
        },
        "etiam",
        ["laoreet", "tincidunt"],
        ["vestibulum", "ante"]
      ]
    },
    ipsum: "primis"
  }
};
ReactDOM.createRoot(document.getElementById("root")).render(
  <TreeView data={data} name="data" />
);
```

请点击右下角的“Go Live”在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
