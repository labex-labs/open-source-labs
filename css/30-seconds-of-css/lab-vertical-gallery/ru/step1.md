# Галерея изображений с вертикальной прокруткой

Файлы `index.html` и `style.css` уже предоставлены в виртуальной машине (VM).

Этот код создает горизонтально прокручиваемую галерею изображений. Следующие шаги были выполнены:

1. Сетка (макет) контейнера настроена с использованием `display: flex` и `justify-content: center`.
2. Сетка (макет) слайдов настроена с использованием `display: flex` и `flex-direction: column`.
3. Создан эффект "прилипания" (snap effect) при вертикальной прокрутке с использованием `scroll-snap-type: y mandatory` и `overscroll-behavior-y: contain`. Элементы прилипают к началу контейнера с использованием `scroll-snap-align: start`.
4. Полосы прокрутки скрыты с использованием `scrollbar-width: none` и стилизации псевдоэлемента `::-webkit-scrollbar` в `display: none`.
5. Определена функция `scrollToElement` с использованием `Element.scrollTo()`, чтобы прокрутить галерею к заданному элементу.
6. Элемент `.thumbnails` заполнен с использованием `Array.prototype.map()` и `Array.prototype.join()`. Каждый миниатюрный элемент (миниатюра) получает атрибут `data-id` с индексом изображения.
7. Для каждого миниатюрного элемента зарегистрирован обработчик события `'click'` с использованием `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` и функции `scrollToElement`.
8. Зарегистрирован обработчик события `'scroll'` с использованием `Document.querySelector()` и `EventTarget.addEventListener()`. Элементы `.thumbnails` и `.scrollbar` обновляются в соответствии с текущим положением прокрутки с использованием функции `scrollThumb`.

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

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
