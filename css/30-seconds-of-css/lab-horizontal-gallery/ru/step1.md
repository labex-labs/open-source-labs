# Галерея изображений с горизонтальной прокруткой

`index.html` и `style.css` уже предоставлены в виртуальной машине (VM).

Вот инструкции по созданию горизонтально прокручиваемой галереи изображений:

1. Чтобы разместить `.thumbnails` внизу контейнера, задайте `position: absolute; bottom: 8px;` для класса `.thumbnails`.
2. Чтобы создать эффект "прилипания" при горизонтальной прокрутке, используйте `scroll-snap-type: x mandatory` и `overscroll-behavior-x: contain`. Прикрепите элементы к началу контейнера с помощью `scroll-snap-align: start`.
3. Скрыть полосы прокрутки можно, установив `scrollbar-width: none`. Чтобы стилизовать псевдоэлемент `::-webkit-scrollbar`, добавьте `display: none;`.
4. Определите функцию `scrollToElement` с использованием `Element.scrollTo()`, которая прокручивает галерею к заданному элементу.
5. Заполните элемент `.thumbnails` с использованием `Array.prototype.map()` и `Array.prototype.join()`. Присвойте каждому миниатюре атрибут `data-id` с индексом изображения.
6. Зарегистрируйте обработчик события `'click'` для каждой миниатюры с использованием `Document.querySelectorAll()` и `Array.prototype.forEach()`. Используйте `EventTarget.addEventListener()` и функцию `scrollToElement`.
7. Зарегистрируйте обработчик события `'scroll'` с использованием `Document.querySelector()` и `EventTarget.addEventListener()`. Обновите элемент `.thumbnails`, чтобы он соответствовал текущей позиции прокрутки, используя функцию `highlightThumbnail`.

Вот HTML - код для галереи:

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

Вот CSS - код для галереи:

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

И вот JavaScript - код для галереи:

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

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб - страницу.
