# 锯齿状背景图案

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建锯齿状背景图案，请按以下步骤操作：

1. 使用 `background-color` 设置白色背景。
2. 使用带有四个 `linear-gradient()` 值的 `background-image` 创建锯齿图案的各个部分。
3. 使用 `background-size` 指定图案的大小。
4. 使用 `background-position` 将图案的各个部分放置在正确的位置。
5. 要重复图案，请使用 `background-repeat`。
6. **注意**：仅为演示目的，元素的 `height` 和 `width` 是固定的。

以下是一个示例代码片段：

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%), linear-gradient(
      315deg,
      #000 25%,
      transparent 25%
    ), linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
