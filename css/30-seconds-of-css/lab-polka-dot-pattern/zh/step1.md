# 圆点背景图案

虚拟机中已提供 `index.html` 和 `style.css`。

要创建圆点背景图案，你可以遵循以下步骤：

1. 将 `background-color` 属性设置为黑色。
2. 使用 `background-image` 属性和两个 `radial-gradient()` 值来创建两个圆点。
3. 使用 `background-size` 属性指定图案的大小。使用 `background-position` 来适当地放置这两个渐变。
4. 将 `background-repeat` 设置为 `repeat`。
5. 请注意，元素固定的 `height` 和 `width` 仅用于演示目的。

以下是一个带有类 `polka-dot` 的 div 元素的示例 HTML 代码：

```html
<div class="polka-dot"></div>
```

以及相应的 CSS 代码：

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新 **Web 8080** 标签页来预览网页。
