# 子元素获得焦点

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在表单的任何子元素获得焦点时更改表单的外观，请使用伪类 `:focus-within` 为父元素应用样式。例如，在给定的 HTML 代码中，如果任何输入字段获得焦点，`form` 元素将具有绿色背景。要为子元素应用样式，请使用适当的 CSS 选择器，如 `label` 和 `input`。

```html
<form>
  <label for="username">用户名：</label>
  <input id="username" type="text" />
  <br />
  <label for="password">密码：</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

请点击右下角的“上线”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
