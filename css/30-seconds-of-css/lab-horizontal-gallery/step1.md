# Image Gallery With Horizontal Scroll

`index.html` and `style.css` have already been provided in the VM.

Here are revised instructions for creating a horizontally scrollable image gallery:

1. To position the `.thumbnails` at the bottom of the container, set `position: absolute; bottom: 8px;` for the `.thumbnails` class.
2. To create a snap effect on horizontal scroll, use `scroll-snap-type: x mandatory` and `overscroll-behavior-x: contain`. Snap elements to the start of the container using `scroll-snap-align: start`.
3. Hide scrollbars by setting `scrollbar-width: none`. To style the pseudo-element `::-webkit-scrollbar`, add `display: none;`.
4. Define a `scrollToElement` function using `Element.scrollTo()` that scrolls the gallery to the given item.
5. Populate the `.thumbnails` element using `Array.prototype.map()` and `Array.prototype.join()`. Give each thumbnail a `data-id` attribute with the index of the image.
6. Register a handler for the `'click'` event on each thumbnail using `Document.querySelectorAll()` and `Array.prototype.forEach()`. Use `EventTarget.addEventListener()` and the `scrollToElement` function.
7. Register a handler for the `'scroll'` event using `Document.querySelector()` and `EventTarget.addEventListener()`. Update the `.thumbnails` element to match the current scroll position using the `highlightThumbnail` function.

Here is the HTML code for the gallery:

```html
<div class="gallery-container">
  <div class="thumbnails"></div>
  <div class="slides">
    <div><img src="https://picsum.photos/id/1067/540/720"></div>
    <div><img src="https://picsum.photos/id/122/540/720"></div>
    <div><img src="https://picsum.photos/id/188/540/720"></div>
    <div><img src="https://picsum.photos/id/249/540/720"></div>
    <div><img src="https://picsum.photos/id/257/540/720"></div>
    <div><img src="https://picsum.photos/id/259/540/720"></div>
    <div><img src="https://picsum.photos/id/283/540/720"></div>
    <div><img src="https://picsum.photos/id/288/540/720"></div>
    <div><img src="https://picsum.photos/id/299/540/720"></div>
  </div>
</div>
```

Here is the CSS code for the gallery:

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

And here is the JavaScript code for the gallery:

```js
const slideGallery = document.querySelector('.slides');
const slides = slideGallery.querySelectorAll('div');
const thumbnailContainer = document.querySelector('.thumbnails');
const slideCount = slides.length;
const slideWidth = 540;

const highlightThumbnail = () => {
  thumbnailContainer
    .querySelectorAll('div.highlighted')
    .forEach(el => el.classList.remove('highlighted'));
  const index = Math.floor(slideGallery.scrollLeft / slideWidth);
  thumbnailContainer
    .querySelector(`div[data-id="${index}"]`)
    .classList.add('highlighted');
};

const scrollToElement = el => {
  const index = parseInt(el.dataset.id, 10);
  slideGallery.scrollTo(index * slideWidth, 0);
};

thumbnailContainer.innerHTML += [...slides]
  .map((slide, i) => `<div data-id="${i}"></div>`)
  .join('');

thumbnailContainer.querySelectorAll('div').forEach(el => {
  el.addEventListener('click', () => scrollToElement(el));
});

slideGallery.addEventListener('scroll', e => highlightThumbnail());

highlightThumbnail();
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
