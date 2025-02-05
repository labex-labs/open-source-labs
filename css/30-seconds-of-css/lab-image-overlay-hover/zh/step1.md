# 悬停时的图像叠加

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在悬停时显示图像叠加效果，请执行以下步骤：

1. 分别对叠加层的顶部和底部栏使用 `::before` 和 `::after` 伪元素。设置它们的 `opacity`、`transform` 和 `transition` 以产生所需效果。
2. 对叠加层的文本使用 `<figcaption>`。设置 `display: flex`、`flex-direction: column` 和 `justify-content: center` 以使文本在图像中居中。
3. 使用 `:hover` 伪选择器来更新所有元素的 `opacity` 和 `transform` 并显示叠加层。

以下是要使用的 HTML 代码：

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

以下是要使用的 CSS 代码：

```css
.hover-img {
  display: inline-block;
  margin: 8px;
  width: 100%;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  background-color: #000;
  color: #fff;
}

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
  transition: all 0.3s ease;
}

.hover-img::before {
  content: "";
  top: 0;
  bottom: auto;
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
