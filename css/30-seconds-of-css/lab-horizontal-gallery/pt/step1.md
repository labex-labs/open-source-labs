# Galeria de Imagens com Rolagem Horizontal

`index.html` e `style.css` já foram fornecidos na VM.

Aqui estão as instruções para criar uma galeria de imagens com rolagem horizontal:

1. Para posicionar `.thumbnails` na parte inferior do contêiner, defina `position: absolute; bottom: 8px;` para a classe `.thumbnails`.
2. Para criar um efeito de "snap" na rolagem horizontal, use `scroll-snap-type: x mandatory` e `overscroll-behavior-x: contain`. Faça com que os elementos se encaixem no início do contêiner usando `scroll-snap-align: start`.
3. Oculte as barras de rolagem definindo `scrollbar-width: none`. Para estilizar o pseudo-elemento `::-webkit-scrollbar`, adicione `display: none;`.
4. Defina uma função `scrollToElement` usando `Element.scrollTo()` que role a galeria para o item fornecido.
5. Preencha o elemento `.thumbnails` usando `Array.prototype.map()` e `Array.prototype.join()`. Dê a cada miniatura um atributo `data-id` com o índice da imagem.
6. Registre um manipulador para o evento `'click'` em cada miniatura usando `Document.querySelectorAll()` e `Array.prototype.forEach()`. Use `EventTarget.addEventListener()` e a função `scrollToElement`.
7. Registre um manipulador para o evento `'scroll'` usando `Document.querySelector()` e `EventTarget.addEventListener()`. Atualize o elemento `.thumbnails` para corresponder à posição atual da rolagem usando a função `highlightThumbnail`.

Aqui está o código HTML para a galeria:

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

Aqui está o código CSS para a galeria:

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

E aqui está o código JavaScript para a galeria:

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

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
