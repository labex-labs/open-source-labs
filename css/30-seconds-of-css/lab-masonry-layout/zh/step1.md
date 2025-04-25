# 砖石布局

虚拟机中已经提供了`index.html`和`style.css`。

要创建砖石风格的布局，使用`.masonry-container`作为主容器，并添加`.masonry-columns`作为内部容器，将`.masonry-brick`元素放置在其中。该布局由相互堆叠的“砖块”组成，完美契合。垂直布局的`width`和水平布局的`height`可以固定。

为确保布局正常流动，对`.masonry-brick`元素应用`display: block`。使用`:first-child`伪元素选择器为第一个元素应用不同的`margin`，以考虑其定位。

为了实现更大的灵活性和响应性，使用 CSS 变量和媒体查询。`.masonry-container`有用于列数和间距的 CSS 变量。列数由媒体查询控制，这些媒体查询为不同的屏幕尺寸指定不同的列数和宽度。

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新**Web 8080**标签页来预览网页。
