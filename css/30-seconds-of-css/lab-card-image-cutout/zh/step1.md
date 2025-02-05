# 带图像剪裁效果的卡片

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个带有图像剪裁效果的卡片，请按照以下步骤操作：

1. 使用 `background` 属性为 `.container` 元素添加彩色背景。
2. 创建一个 `.card` 元素，并在其中添加一个 `figure` 元素，包含所需的图像和任何其他内容。
3. 使用 `::before` 伪元素为 `figure` 元素添加 `border`。将边框颜色设置为与 `.container` 元素的 `background` 颜色匹配，以在 `.card` 中营造出剪裁效果的错觉。

以下是该卡片的 HTML 代码示例：

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

以及相应的 CSS 代码：

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
