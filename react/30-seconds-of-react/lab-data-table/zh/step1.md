# 数据表格

> 虚拟机中已提供了 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

创建一个包含两列（“ID”和“值”）的表格元素，其中每一行都从基本值数组动态生成。

要实现这一点，使用 `Array.prototype.map()` 方法创建一个新的 JSX 元素数组，将输入 `data` 数组中的每个项目表示为一个带有适当 `key` 的 `<tr>` 元素。在每个 `<tr>` 中，添加两个 `<td>` 元素，分别显示该行的索引和值。

以下是一个示例实现：

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>值</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

例如，要将此组件与人员名字数组一起使用，可以如下调用它：

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页以预览网页。
