# 带前缀的输入框

虚拟机中已提供了`index.html`和`style.css`。

要创建一个带有可视化、不可编辑前缀的输入框，请执行以下步骤：

1. 使用`display: flex`创建一个类名为`.input-box`的容器元素。
2. 从`<input>`字段中移除边框和轮廓，并将它们应用于父元素，使其看起来像一个输入框。
3. 使用`:focus-within`伪类选择器，以便在用户与`<input>`字段交互时相应地设置父元素的样式。

以下是 HTML 代码：

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

以下是 CSS 代码：

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
