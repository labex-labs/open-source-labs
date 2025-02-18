# Galería de imágenes con desplazamiento vertical

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Este código crea una galería de imágenes desplazable horizontalmente. Se realizan los siguientes pasos:

1. Se configura el diseño del contenedor utilizando `display: flex` y `justify-content: center`.
2. Se configura el diseño de las diapositivas (slides) utilizando `display: flex` y `flex-direction: column`.
3. Se crea un efecto de ajuste (snap) al desplazarse verticalmente utilizando `scroll-snap-type: y mandatory` y `overscroll-behavior-y: contain`. Los elementos se ajustan al inicio del contenedor utilizando `scroll-snap-align: start`.
4. Se ocultan las barras de desplazamiento utilizando `scrollbar-width: none` y dando estilo al pseudo-elemento `::-webkit-scrollbar` para que `display: none`.
5. Se define una función `scrollToElement` utilizando `Element.scrollTo()` para desplazar la galería hasta el elemento dado.
6. El elemento `.thumbnails` se llena utilizando `Array.prototype.map()` y `Array.prototype.join()`. A cada miniatura (thumbnail) se le da un atributo `data-id` con el índice de la imagen.
7. Se registra un controlador para el evento `'click'` en cada miniatura utilizando `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` y la función `scrollToElement`.
8. Se registra un controlador para el evento `'scroll'` utilizando `Document.querySelector()` y `EventTarget.addEventListener()`. Los elementos `.thumbnails` y `.scrollbar` se actualizan para que coincidan con la posición actual de desplazamiento utilizando la función `scrollThumb`.

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

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
