# Image Gallery With Vertical Scroll

`index.html` and `style.css` have already been provided in the VM.

This code creates a horizontally scrollable image gallery. The following steps are taken:

1. The layout for the container is set up using `display: flex` and `justify-content: center`.
2. The layout for the slides is set up using `display: flex` and `flex-direction: column`.
3. A snap effect is created on vertical scroll using `scroll-snap-type: y mandatory` and `overscroll-behavior-y: contain`. Elements are snapped to the start of the container using `scroll-snap-align: start`.
4. Scrollbars are hidden using `scrollbar-width: none` and styling the pseudo-element `::-webkit-scrollbar` to `display: none`.
5. A `scrollToElement` function is defined using `Element.scrollTo()` to scroll the gallery to the given item.
6. The `.thumbnails` element is populated using `Array.prototype.map()` and `Array.prototype.join()`. Each thumbnail is given a `data-id` attribute with the index of the image.
7. A handler for the `'click'` event is registered on each thumbnail using `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()`, and the `scrollToElement` function.
8. A handler for the `'scroll'` event is registered using `Document.querySelector()` and `EventTarget.addEventListener()`. The `.thumbnails` and `.scrollbar` elements are updated to match the current scroll position using the `scrollThumb` function.

HTML:

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

CSS:

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

JavaScript:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
