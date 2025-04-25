# 水平滚动捕捉

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个水平可滚动的容器，使其在滚动时捕捉到元素，请按照以下步骤操作：

1. 使用 `display: grid` 和 `grid-auto-flow: column` 创建水平布局。
2. 使用 `scroll-snap-type: x mandatory` 和 `overscroll-behavior-x: contain` 在水平滚动时创建捕捉效果。
3. 将 `scroll-snap-align` 更改为 `start`、`stop` 或 `center` 以调整捕捉对齐方式。

以下是你可以使用的示例 HTML 和 CSS 代码：

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
