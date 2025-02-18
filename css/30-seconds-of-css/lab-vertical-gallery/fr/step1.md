# Image Gallery With Vertical Scroll

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Ce code crée une galerie d'images défilable verticalement. Les étapes suivantes sont effectuées :

1. La mise en page du conteneur est configurée en utilisant `display: flex` et `justify-content: center`.
2. La mise en page des diapositives (slides) est configurée en utilisant `display: flex` et `flex-direction: column`.
3. Un effet de capture (snap) est créé lors du défilement vertical en utilisant `scroll-snap-type: y mandatory` et `overscroll-behavior-y: contain`. Les éléments sont capturés au début du conteneur en utilisant `scroll-snap-align: start`.
4. Les barres de défilement sont masquées en utilisant `scrollbar-width: none` et en stylisant l'élément pseudo `::-webkit-scrollbar` pour qu'il ait `display: none`.
5. Une fonction `scrollToElement` est définie en utilisant `Element.scrollTo()` pour faire défiler la galerie jusqu'à l'élément donné.
6. L'élément `.thumbnails` est rempli en utilisant `Array.prototype.map()` et `Array.prototype.join()`. Chaque miniature (thumbnail) est dotée d'un attribut `data-id` avec l'index de l'image.
7. Un gestionnaire pour l'événement `'click'` est enregistré sur chaque miniature en utilisant `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` et la fonction `scrollToElement`.
8. Un gestionnaire pour l'événement `'scroll'` est enregistré en utilisant `Document.querySelector()` et `EventTarget.addEventListener()`. Les éléments `.thumbnails` et `.scrollbar` sont mis à jour pour correspondre à la position de défilement actuelle en utilisant la fonction `scrollThumb`.

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

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
