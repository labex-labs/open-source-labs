# Galerie d'images avec défilement horizontal

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Voici les instructions pour créer une galerie d'images défilante horizontalement :

1. Pour positionner la classe `.thumbnails` en bas du conteneur, définissez `position: absolute; bottom: 8px;` pour la classe `.thumbnails`.
2. Pour créer un effet de "snap" (accrochage) lors du défilement horizontal, utilisez `scroll-snap-type: x mandatory` et `overscroll-behavior-x: contain`. Accrochez les éléments au début du conteneur en utilisant `scroll-snap-align: start`.
3. Masquez les barres de défilement en définissant `scrollbar-width: none`. Pour styliser l'élément pseudo `::-webkit-scrollbar`, ajoutez `display: none;`.
4. Définissez une fonction `scrollToElement` en utilisant `Element.scrollTo()` qui fait défiler la galerie jusqu'à l'élément donné.
5. Remplissez l'élément `.thumbnails` en utilisant `Array.prototype.map()` et `Array.prototype.join()`. Donnez à chaque miniature un attribut `data-id` avec l'index de l'image.
6. Enregistrez un gestionnaire pour l'événement `'click'` sur chaque miniature en utilisant `Document.querySelectorAll()` et `Array.prototype.forEach()`. Utilisez `EventTarget.addEventListener()` et la fonction `scrollToElement`.
7. Enregistrez un gestionnaire pour l'événement `'scroll'` en utilisant `Document.querySelector()` et `EventTarget.addEventListener()`. Mettez à jour l'élément `.thumbnails` pour qu'il corresponde à la position de défilement actuelle en utilisant la fonction `highlightThumbnail`.

Voici le code HTML de la galerie :

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

Voici le code CSS de la galerie :

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

Et voici le code JavaScript de la galerie :

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

Cliquez sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
