# Galería de imágenes con desplazamiento horizontal

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

A continuación, se presentan las instrucciones para crear una galería de imágenes desplazable horizontalmente:

1. Para posicionar la clase `.thumbnails` en la parte inferior del contenedor, establece `position: absolute; bottom: 8px;` para la clase `.thumbnails`.
2. Para crear un efecto de ajuste (snap) en el desplazamiento horizontal, utiliza `scroll-snap-type: x mandatory` y `overscroll-behavior-x: contain`. Ajusta los elementos al inicio del contenedor utilizando `scroll-snap-align: start`.
3. Oculta las barras de desplazamiento estableciendo `scrollbar-width: none`. Para dar estilo al pseudo-elemento `::-webkit-scrollbar`, agrega `display: none;`.
4. Define una función `scrollToElement` utilizando `Element.scrollTo()` que desplace la galería hasta el elemento dado.
5. Rellena el elemento `.thumbnails` utilizando `Array.prototype.map()` y `Array.prototype.join()`. Da a cada miniatura un atributo `data-id` con el índice de la imagen.
6. Registra un controlador para el evento `'click'` en cada miniatura utilizando `Document.querySelectorAll()` y `Array.prototype.forEach()`. Utiliza `EventTarget.addEventListener()` y la función `scrollToElement`.
7. Registra un controlador para el evento `'scroll'` utilizando `Document.querySelector()` y `EventTarget.addEventListener()`. Actualiza el elemento `.thumbnails` para que coincida con la posición actual de desplazamiento utilizando la función `highlightThumbnail`.

A continuación, se muestra el código HTML de la galería:

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

A continuación, se muestra el código CSS de la galería:

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

Y aquí está el código JavaScript de la galería:

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

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
