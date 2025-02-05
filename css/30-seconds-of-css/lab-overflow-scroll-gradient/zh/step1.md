# 溢出滚动渐变

虚拟机中已经提供了 `index.html` 和 `style.css`。

要为溢出元素添加渐变效果，并表明还有更多内容需要滚动，请按照以下步骤操作：

1. 使用 `::after` 伪元素创建一个从 `透明` 渐变到 `白色`（从上到下）的 `linear-gradient()`。
2. 使用 `position: absolute`、`width` 和 `height` 在其父元素中定位和调整伪元素的大小。
3. 使用 `pointer-events: none` 将伪元素排除在鼠标事件之外，使其后的文本仍可选择/交互。

以下是一个 HTML 和 CSS 代码片段示例：

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行 Web 服务。然后，你可以刷新“Web 8080”标签页来预览网页。
