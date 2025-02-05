# 带有垂直滚动条的图像画廊

虚拟机中已经提供了 `index.html` 和 `style.css`。

这段代码创建了一个可水平滚动的图像画廊。具体步骤如下：

1. 使用 `display: flex` 和 `justify-content: center` 设置容器的布局。
2. 使用 `display: flex` 和 `flex-direction: column` 设置幻灯片的布局。
3. 使用 `scroll-snap-type: y mandatory` 和 `overscroll-behavior-y: contain` 在垂直滚动时创建捕捉效果。使用 `scroll-snap-align: start` 将元素捕捉到容器的起始位置。
4. 使用 `scrollbar-width: none` 隐藏滚动条，并将伪元素 `::-webkit-scrollbar` 的样式设置为 `display: none`。
5. 使用 `Element.scrollTo()` 定义一个 `scrollToElement` 函数，用于将画廊滚动到指定的项目。
6. 使用 `Array.prototype.map()` 和 `Array.prototype.join()` 填充 `.thumbnails` 元素。每个缩略图都被赋予一个带有图像索引的 `data-id` 属性。
7. 使用 `Document.querySelectorAll()`、`Array.prototype.forEach()`、`EventTarget.addEventListener()` 和 `scrollToElement` 函数为每个缩略图注册一个 `'click'` 事件的处理程序。
8. 使用 `Document.querySelector()` 和 `EventTarget.addEventListener()` 注册一个 `'scroll'` 事件的处理程序。使用 `scrollThumb` 函数更新 `.thumbnails` 和 `.scrollbar` 元素，以匹配当前的滚动位置。

HTML：

```html
<div class="gallery-container">
  <div class="thumbnails"></div>
  <div class="scrollbar">
    <div class="thumb"></div>
  </div>
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

CSS：

```css
.gallery-container {
  display: flex;
  justify-content: center;
}

.thumbnails {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.thumbnails img {
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.scrollbar {
  width: 1px;
  height: 720px;
  background: #ccc;
  display: block;
  margin: 0 0 0 8px;
}

.thumb {
  width: 1px;
  position: absolute;
  height: 0;
  background: #000;
}

.slides {
  margin: 0 16px;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
  width: calc(540px + 1rem);
  padding: 0 0.25rem;
  height: 720px;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-snap-type: y mandatory;
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

JavaScript：

```js
const slideGallery = document.querySelector(".slides");
const slides = slideGallery.querySelectorAll("div");
const scrollbarThumb = document.querySelector(".thumb");
const slideCount = slides.length;
const slideHeight = 720;
const marginTop = 16;

const scrollThumb = () => {
  const index = Math.floor(slideGallery.scrollTop / slideHeight);
  scrollbarThumb.style.height = `${((index + 1) / slideCount) * slideHeight}px`;
};

const scrollToElement = (el) => {
  const index = parseInt(el.dataset.id, 10);
  slideGallery.scrollTo(0, index * slideHeight + marginTop);
};

document.querySelector(".thumbnails").innerHTML += [...slides]
  .map(
    (slide, i) => `<img src="${slide.querySelector("img").src}" data-id="${i}">`
  )
  .join("");

document.querySelectorAll(".thumbnails img").forEach((el) => {
  el.addEventListener("click", () => scrollToElement(el));
});

slideGallery.addEventListener("scroll", (e) => scrollThumb());

scrollThumb();
```

请点击右下角的“Go Live”以在端口8080上运行网络服务。然后，你可以刷新“Web 8080”标签页来预览网页。
