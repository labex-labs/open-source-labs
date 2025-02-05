# 悬停在图像上时显示菜单

虚拟机中已经提供了 `index.html` 和 `style.css`。

要在用户悬停在图像上时显示菜单覆盖层，请使用 `<figure>` 包裹 `<img>` 元素，并使用一个 `<div>` 元素来包含菜单链接。应用以下 CSS 属性来在悬停时为图像设置动画效果，创建滑动效果：

- `opacity`
- `right`
  将 `<div>` 的 `left` 属性设置为该元素宽度的负值。当悬停在父元素上时，将其重置为 `0` 以滑入菜单。最后，在 `<div>` 上使用 `display: flex`、`flex-direction: column` 和 `justify-content: center` 来垂直居中菜单项。

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">首页</a>
    <a href="#">定价</a>
    <a href="#">关于</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

请点击右下角的“上线”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
