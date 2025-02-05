# 棋盘格背景图案

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建棋盘格背景图案，请按照以下步骤操作：

1. 将 `background-color` 属性设置为白色。
2. 使用 `background-image` 并搭配两个 `linear-gradient()` 值，每个值使用不同的角度来创建棋盘格图案。例如，将一个角度设置为 `45deg`，另一个设置为 `-45deg`。
3. 使用 `background-size` 指定图案的大小。例如，`60px 60px` 将创建一个 60×60 像素的图案。
4. 使用 `background-repeat` 设置图案的重复方式。例如，`repeat` 将使图案在两个方向上重复。
5. 请注意，为了演示目的，元素的 `height` 和 `width` 属性固定为 240px。

这是一个带有 `.checkerboard` 类的 HTML 元素示例：

```html
<div class="checkerboard"></div>
```

这是相应的 CSS：

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
