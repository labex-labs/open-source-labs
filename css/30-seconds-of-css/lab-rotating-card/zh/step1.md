# 旋转卡片

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个悬停时旋转的双面卡片，请按照以下步骤操作：

1. 将卡片的 `backface-visibility` 设置为 `none`，以防止背面默认可见。
2. 初始时，为卡片的背面设置 `rotateY(-180deg)`，为卡片的正面设置 `rotateY(0deg)`。
3. 悬停时，为卡片的正面设置 `rotateY(180deg)`，为卡片的背面设置 `rotateY(0deg)`。
4. 设置适当的 `perspective` 值以创建旋转效果。

以下是一个 HTML 和 CSS 代码示例：

```html
<div class="card">
  <div class="card-side front">
    <div>正面</div>
  </div>
  <div class="card-side back">
    <div>背面</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

请点击右下角的“Go Live”以在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
