# 带有水平滚动条的图像画廊

虚拟机中已经提供了 `index.html` 和 `style.css`。

以下是创建水平可滚动图像画廊的步骤说明：

1. 要将 `.thumbnails` 定位在容器底部，为 `.thumbnails` 类设置 `position: absolute; bottom: 8px;`。
2. 要在水平滚动时创建捕捉效果，使用 `scroll-snap-type: x mandatory` 和 `overscroll-behavior-x: contain`。使用 `scroll-snap-align: start` 将元素捕捉到容器的起始位置。
3. 通过设置 `scrollbar-width: none` 隐藏滚动条。要设置伪元素 `::-webkit-scrollbar` 的样式，添加 `display: none;`。
4. 使用 `Element.scrollTo()` 定义一个 `scrollToElement` 函数，该函数将画廊滚动到给定的项目。
5. 使用 `Array.prototype.map()` 和 `Array.prototype.join()` 填充 `.thumbnails` 元素。为每个缩略图赋予一个带有图像索引的 `data-id` 属性。
6. 使用 `Document.querySelectorAll()` 和 `Array.prototype.forEach()` 为每个缩略图注册一个 `'click'` 事件的处理程序。使用 `EventTarget.addEventListener()` 和 `scrollToElement` 函数。
7. 使用 `Document.querySelector()` 和 `EventTarget.addEventListener()` 为 `'scroll'` 事件注册一个处理程序。使用 `highlightThumbnail` 函数更新 `.thumbnails` 元素以匹配当前滚动位置。

以下是画廊的 HTML 代码：

```html
<div class="gallery-container">
  <div class="thumbnails"></div>
  <div class="slides">
    <div><img src="https://picsum.photos/id/1067/540/720" /></div>
    <div><img src="https://picsum.photos/id/122/540/720" /></div>
    <div><img src="https://picsum.photos/id/188/540/720" /></div>
    <div><img src="https://picsum.photos/id/249/540/720" /></div>
    <div><img src="https://picsum.photos/id/257/540/720" /></div>
    <div><img src="https://picsum.photos/id/259/540/720" /></div>
    <div><img src="https://picsum.photos/id/283/540/720" /></div>
    <div><img src="https://picsum.photos/id/288/540/720" /></div>
    <div><img src="https://picsum.photos/id/299/540/720" /></div>
  </div>
</div>
```

以下是画廊的 CSS 代码：

```css
.gallery-container {
  position: relative;
  display: flex;
  justify-content: center;
}

.thumbnails {
  position: absolute;
  bottom: 8px;
  display: flex;
  flex-direction: row;
  gap: 6px;
}

.thumbnails div {
  width: 8px;
  height: 8px;
  cursor: pointer;
  background: #aaa;
  border-radius: 100%;
}

.thumbnails div.highlighted {
  background-color: #777;
}

.slides {
  margin: 0 16px;
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  width: 540px;
  padding: 0 0.25rem;
  height: 720px;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
}

.slides > div {
  scroll-snap-align: start;
}

.slides img {
  width: 540px;
  object-fit: contain;
}

.slides::-webkit-scrollbar {
  display: none;
}
```

以下是画廊的 JavaScript 代码：

```js
const slideGallery = document.querySelector(".slides");
const slides = slideGallery.querySelectorAll("div");
const thumbnailContainer = document.querySelector(".thumbnails");
const slideCount = slides.length;
const slideWidth = 540;

const highlightThumbnail = () => {
  thumbnailContainer
    .querySelectorAll("div.highlighted")
    .forEach((el) => el.classList.remove("highlighted"));
  const index = Math.floor(slideGallery.scrollLeft / slideWidth);
  thumbnailContainer
    .querySelector(`div[data-id="${index}"]`)
    .classList.add("highlighted");
};

const scrollToElement = (el) => {
  const index = parseInt(el.dataset.id, 10);
  slideGallery.scrollTo(index * slideWidth, 0);
};

thumbnailContainer.innerHTML += [...slides]
  .map((slide, i) => `<div data-id="${i}"></div>`)
  .join("");

thumbnailContainer.querySelectorAll("div").forEach((el) => {
  el.addEventListener("click", () => scrollToElement(el));
});

slideGallery.addEventListener("scroll", (e) => highlightThumbnail());

highlightThumbnail();
```

请点击右下角的“Go Live”在端口 8080 上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
