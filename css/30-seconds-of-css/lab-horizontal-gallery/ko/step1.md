# 수평 스크롤 이미지 갤러리

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

수평 스크롤 가능한 이미지 갤러리를 만드는 방법에 대한 지침은 다음과 같습니다.

1. `.thumbnails`를 컨테이너 하단에 배치하려면 `.thumbnails` 클래스에 `position: absolute; bottom: 8px;`를 설정합니다.
2. 수평 스크롤 시 스냅 효과를 만들려면 `scroll-snap-type: x mandatory` 및 `overscroll-behavior-x: contain`을 사용합니다. `scroll-snap-align: start`를 사용하여 요소를 컨테이너 시작 부분에 스냅합니다.
3. `scrollbar-width: none`을 설정하여 스크롤바를 숨깁니다. 가상 요소 `::-webkit-scrollbar`의 스타일을 지정하려면 `display: none;`을 추가합니다.
4. `Element.scrollTo()`를 사용하여 갤러리를 주어진 항목으로 스크롤하는 `scrollToElement` 함수를 정의합니다.
5. `Array.prototype.map()` 및 `Array.prototype.join()`을 사용하여 `.thumbnails` 요소를 채웁니다. 각 썸네일에 이미지의 인덱스를 가진 `data-id` 속성을 부여합니다.
6. `Document.querySelectorAll()` 및 `Array.prototype.forEach()`를 사용하여 각 썸네일에 대한 `'click'` 이벤트의 핸들러를 등록합니다. `EventTarget.addEventListener()` 및 `scrollToElement` 함수를 사용합니다.
7. `Document.querySelector()` 및 `EventTarget.addEventListener()`를 사용하여 `'scroll'` 이벤트의 핸들러를 등록합니다. `highlightThumbnail` 함수를 사용하여 현재 스크롤 위치에 맞게 `.thumbnails` 요소를 업데이트합니다.

다음은 갤러리에 대한 HTML 코드입니다.

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

다음은 갤러리에 대한 CSS 코드입니다.

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

다음은 갤러리에 대한 JavaScript 코드입니다.

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

오른쪽 하단 모서리에서 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
