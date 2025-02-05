# 悬停阴影框动画

虚拟机中已提供了`index.html`和`style.css`。

要在文本悬停时在其周围创建一个阴影框，请执行以下步骤：

1. 设置`transform: perspective(1px)`，通过影响Z平面与用户之间的距离，为元素赋予3D空间，并设置`translateZ(0)`，以便在3D空间中沿z轴重新定位`p`元素。
2. 使用`box-shadow`使框透明。
3. 通过使用`transition-property`属性，为`box-shadow`和`transform`启用过渡效果。
4. 使用`:hover`、`:active`和`:focus`伪类选择器，应用新的`box-shadow`和`transform: scale(1.2)`来更改文本的比例。
5. 将类`hover-shadow-box-animation`添加到`p`元素。

以下是HTML代码：

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

以下是CSS代码：

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

请点击右下角的“Go Live”，在端口8080上运行Web服务。然后，你可以刷新“Web 8080”标签页来预览网页。
