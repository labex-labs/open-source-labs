# 条纹背景图案

虚拟机中已提供 `index.html` 和 `style.css`。

此代码在白色背景上创建垂直条纹图案。

要创建该图案：

- 将 `background-color` 属性设置为白色。
- 使用带有 `linear-gradient()` 值的 `background-image` 创建垂直条纹。
- 设置 `background-size` 属性以指定每条条纹的大小。
- 将 `background-repeat` 设置为 `repeat` 以使图案填充元素。

请注意，元素固定的 `width` 和 `height` 仅用于演示目的。

以下是一个示例代码片段：

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
