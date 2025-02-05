# 翻转卡片

虚拟机中已经提供了 `index.html` 和 `style.css`。

要创建一个悬停时会翻转的卡片，请按照以下步骤操作：

1. 在 `.container` 元素上设置适当的 `perspective`（透视），以实现翻转效果。
2. 为 `.card` 元素的 `transform` 属性添加一个 `transition`（过渡效果）。
3. 使用 `Document.querySelector()` 选择 `.card` 元素，并为 `mousemove`（鼠标移动）和 `mouseout`（鼠标移出）事件添加事件监听器。
4. 使用 `Element.getBoundingClientRect()` 获取 `.card` 元素的 `x`、`y`、`width` 和 `height`。
5. 计算 `x` 和 `y` 轴上介于 `-1` 和 `1` 之间的相对距离，并通过 `transform` 属性应用它。

以下是卡片的示例 HTML 和 CSS 代码：

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>卡片</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card.content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

以下是添加悬停效果的 JavaScript 代码：

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
