# 垂直滚动捕捉

虚拟机中已经提供了 `index.html` 和 `style.css`。

这段代码创建了一个可滚动的容器，在滚动时会捕捉到各个元素。为实现此效果，采取了以下步骤：

1. 使用 `display: grid` 和 `grid-auto-flow: row` 创建垂直布局。
2. 使用 `scroll-snap-type: y mandatory` 和 `overscroll-behavior-y: contain` 在垂直滚动时创建捕捉效果。
3. 可以使用 `scroll-snap-align` 并搭配 `start`、`stop` 或 `center` 来更改捕捉对齐方式。

以下是 HTML 和 CSS 代码：

```html
<div class="vertical-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640" /></a>
</div>
```

```css
.vertical-snap {
  margin: 0 auto;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
  width: calc(180px + 1rem);
  padding: 1rem;
  height: 480px;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-snap-type: y mandatory;
}

.vertical-snap > a {
  scroll-snap-align: center;
}

.vertical-snap img {
  width: 180px;
  object-fit: contain;
  border-radius: 1rem;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
