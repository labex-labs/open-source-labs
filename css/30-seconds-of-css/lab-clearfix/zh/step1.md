# 清除浮动

虚拟机中已经提供了 `index.html` 和 `style.css`。

在使用 `float` 构建布局时，为确保一个元素能自动清除其浮动子元素，你可以使用 `::after` 伪元素，并应用 `content: ''` 使其能影响布局。此外，使用 `clear: both` 让该元素清除之前的左右浮动。不过，只有在容器中没有非浮动子元素，且在清除浮动的容器之前（但在相同格式化上下文内，例如浮动列）没有高的浮动元素时，此技术才会正常工作。例如：

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

请注意，相比于使用 `float` 构建布局，推荐使用更现代的方法，比如弹性盒布局（flexbox）或网格布局（grid layout）。

请点击右下角的“Go Live”，在端口8080上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
