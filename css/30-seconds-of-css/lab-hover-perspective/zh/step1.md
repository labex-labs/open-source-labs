# 悬停时的透视变换

虚拟机中已经提供了 `index.html` 和 `style.css`。

要对元素创建带有悬停动画的透视变换：

1. 将 `transform` 属性与 `perspective()` 和 `rotateY()` 函数一起使用，为元素应用透视效果。例如，要创建左透视效果，使用 `transform: perspective(1500px) rotateY(15deg);`。要创建右透视效果，使用 `transform: perspective(1500px) rotateY(-15deg);`。

2. 使用 `transition` 属性在元素悬停时为 `transform` 属性设置动画。例如，`transition: transform 1s ease 0s;`。

3. 要从左到右镜像透视效果，在右透视效果中将 `rotateY()` 值改为负数。例如，使用 `transform: perspective(1500px) rotateY(-15deg);`。

示例 HTML：

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

示例 CSS：

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
