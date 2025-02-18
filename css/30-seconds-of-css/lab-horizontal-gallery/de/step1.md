# Bildergalerie mit horizontaler Scrollfunktion

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Hier sind die Anweisungen zur Erstellung einer horizontal scrollbaren Bildergalerie:

1. Um die `.thumbnails` am unteren Rand des Containers zu positionieren, setzen Sie `position: absolute; bottom: 8px;` für die Klasse `.thumbnails`.
2. Um einen Einrast-Effekt beim horizontalen Scrollen zu erstellen, verwenden Sie `scroll-snap-type: x mandatory` und `overscroll-behavior-x: contain`. Rasten Sie die Elemente am Anfang des Containers ein, indem Sie `scroll-snap-align: start` verwenden.
3. Verstecken Sie die Scrollleisten, indem Sie `scrollbar-width: none` setzen. Um das Pseudo-Element `::-webkit-scrollbar` zu gestalten, fügen Sie `display: none;` hinzu.
4. Definieren Sie eine `scrollToElement`-Funktion mit `Element.scrollTo()`, die die Galerie zum angegebenen Element scrollt.
5. Füllen Sie das `.thumbnails`-Element mit `Array.prototype.map()` und `Array.prototype.join()`. Geben Sie jedem Vorschaubild ein `data-id`-Attribut mit dem Index des Bildes.
6. Registrieren Sie einen Handler für das `'click'`-Ereignis auf jedem Vorschaubild mit `Document.querySelectorAll()` und `Array.prototype.forEach()`. Verwenden Sie `EventTarget.addEventListener()` und die `scrollToElement`-Funktion.
7. Registrieren Sie einen Handler für das `'scroll'`-Ereignis mit `Document.querySelector()` und `EventTarget.addEventListener()`. Aktualisieren Sie das `.thumbnails`-Element, um der aktuellen Scrollposition zu entsprechen, indem Sie die `highlightThumbnail`-Funktion verwenden.

Hier ist der HTML-Code für die Galerie:

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

Hier ist der CSS-Code für die Galerie:

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

Und hier ist der JavaScript-Code für die Galerie:

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

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
