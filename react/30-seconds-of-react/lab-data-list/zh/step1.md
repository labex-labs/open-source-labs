# 数据列表

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

此函数从原始值数组渲染项目列表。它可用于根据 `isOrdered` 属性的值有条件地渲染有序列表或无序列表。为了从 `data` 数组渲染每个项目，它使用 `Array.prototype.map()` 为每个项目创建一个带有唯一 `key` 的 `<li>` 元素。

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

以下是如何使用此组件的示例：

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

在此示例中，我们将一个名字数组传递给 `DataList` 组件并渲染两次。第一次，我们渲染一个无序列表，而第二次我们渲染一个有序列表。

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页以预览网页。
