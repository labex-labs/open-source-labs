# 鼠标悬停时显示额外内容

虚拟机中已提供了 `index.html` 和 `style.css`。

要创建一个在鼠标悬停时显示额外内容的卡片，请执行以下步骤：

1. 对卡片使用 `overflow: hidden` 来隐藏任何垂直溢出的元素。
2. 使用 `:hover` 和 `:focus-within` 伪类选择器，以便在元素被悬停、获得焦点或其任何后代获得焦点时更改卡片的样式。
3. 设置 `transition: 0.3s ease all` 以在悬停/聚焦时创建平滑的过渡效果。

以下是该卡片的示例 HTML 代码：

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

以下是为卡片设置样式的 CSS 代码：

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
