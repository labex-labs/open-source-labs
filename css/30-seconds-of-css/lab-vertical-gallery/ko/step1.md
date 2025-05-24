# 수직 스크롤이 있는 이미지 갤러리

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

이 코드는 가로로 스크롤 가능한 이미지 갤러리를 생성합니다. 다음 단계가 수행됩니다.

1. 컨테이너의 레이아웃은 `display: flex` 및 `justify-content: center`를 사용하여 설정됩니다.
2. 슬라이드의 레이아웃은 `display: flex` 및 `flex-direction: column`을 사용하여 설정됩니다.
3. `scroll-snap-type: y mandatory` 및 `overscroll-behavior-y: contain`을 사용하여 수직 스크롤에 스냅 효과가 생성됩니다. 요소는 `scroll-snap-align: start`를 사용하여 컨테이너의 시작 부분에 스냅됩니다.
4. 스크롤바는 `scrollbar-width: none`을 사용하고 가상 요소 `::-webkit-scrollbar`의 스타일을 `display: none`으로 지정하여 숨겨집니다.
5. `scrollToElement` 함수는 `Element.scrollTo()`를 사용하여 지정된 항목으로 갤러리를 스크롤하도록 정의됩니다.
6. `.thumbnails` 요소는 `Array.prototype.map()` 및 `Array.prototype.join()`을 사용하여 채워집니다. 각 썸네일에는 이미지의 인덱스가 있는 `data-id` 속성이 부여됩니다.
7. `'click'` 이벤트에 대한 핸들러는 `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` 및 `scrollToElement` 함수를 사용하여 각 썸네일에 등록됩니다.
8. `'scroll'` 이벤트에 대한 핸들러는 `Document.querySelector()` 및 `EventTarget.addEventListener()`를 사용하여 등록됩니다. `.thumbnails` 및 `.scrollbar` 요소는 `scrollThumb` 함수를 사용하여 현재 스크롤 위치에 맞게 업데이트됩니다.

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

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
