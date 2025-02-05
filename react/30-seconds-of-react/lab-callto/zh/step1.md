# 可调用电话链接

> 虚拟机中已提供 `index.html` 和 `script.js`。一般来说，你只需在 `script.js` 和 `style.css` 中添加代码。

要创建一个用于拨打电话号码的链接，请使用 `Callto` 组件。此组件会创建一个带有适当 `href` 属性的 `<a>` 元素。要渲染该链接，请使用 `phone` 属性指定电话号码，并使用 `children` 属性指定链接文本。

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

要使用 `Callto` 组件，请调用 `ReactDOM.render()` 方法，并传入设置了 `phone` 和 `children` 属性的 `Callto` 元素。

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Call me!</Callto>,
  document.getElementById("root")
);
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
