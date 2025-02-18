# Bildergalerie mit vertikalem Scrollen

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Dieser Code erstellt eine horizontal scrollbare Bildergalerie. Die folgenden Schritte werden durchgeführt:

1. Das Layout für den Container wird mit `display: flex` und `justify-content: center` eingerichtet.
2. Das Layout für die Slides wird mit `display: flex` und `flex-direction: column` eingerichtet.
3. Ein Snap-Effekt wird beim vertikalen Scrollen mit `scroll-snap-type: y mandatory` und `overscroll-behavior-y: contain` erstellt. Die Elemente werden mit `scroll-snap-align: start` am Anfang des Containers ausgerichtet.
4. Die Scrollleisten werden mit `scrollbar-width: none` versteckt und das Pseudo-Element `::-webkit-scrollbar` wird auf `display: none` gesetzt.
5. Eine `scrollToElement`-Funktion wird mit `Element.scrollTo()` definiert, um die Galerie zum angegebenen Element zu scrollen.
6. Das `.thumbnails`-Element wird mit `Array.prototype.map()` und `Array.prototype.join()` befüllt. Jedes Vorschaubild erhält ein `data-id`-Attribut mit dem Index des Bildes.
7. Ein Handler für das `'click'`-Ereignis wird für jedes Vorschaubild mit `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` und der `scrollToElement`-Funktion registriert.
8. Ein Handler für das `'scroll'`-Ereignis wird mit `Document.querySelector()` und `EventTarget.addEventListener()` registriert. Die `.thumbnails`- und `.scrollbar`-Elemente werden mit der `scrollThumb`-Funktion aktualisiert, um der aktuellen Scrollposition zu entsprechen.

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

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
