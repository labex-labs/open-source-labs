# 弹性盒布局居中

虚拟机中已经提供了 `index.html` 和 `style.css`。

要使用弹性盒布局在父元素内水平和垂直居中子元素，请执行以下步骤：

1. 通过将父元素的 `display` 属性设置为 `flex` 来创建弹性盒布局。
2. 使用 `justify-content` 属性并将其值设置为 `center` 来水平居中子元素。
3. 使用 `align-items` 属性并将其值设置为 `center` 来垂直居中子元素。
4. 在父元素内添加子元素。

以下是一个示例代码片段：

```html
<div class="flexbox-centering">
  <div>Centered content.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

请点击右下角的“Go Live”以在端口8080上运行Web服务。然后，你可以刷新“Web 8080”标签页来预览网页。
