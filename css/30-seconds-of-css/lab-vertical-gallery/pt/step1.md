# Galeria de Imagens com Rolagem Vertical

`index.html` e `style.css` já foram fornecidos na VM.

Este código cria uma galeria de imagens com rolagem horizontal. As seguintes etapas são executadas:

1.  O layout para o container é configurado usando `display: flex` e `justify-content: center`.
2.  O layout para os slides é configurado usando `display: flex` e `flex-direction: column`.
3.  Um efeito de "snap" (encaixe) é criado na rolagem vertical usando `scroll-snap-type: y mandatory` e `overscroll-behavior-y: contain`. Os elementos são encaixados no início do container usando `scroll-snap-align: start`.
4.  As barras de rolagem são ocultadas usando `scrollbar-width: none` e estilizando o pseudo-elemento `::-webkit-scrollbar` para `display: none`.
5.  Uma função `scrollToElement` é definida usando `Element.scrollTo()` para rolar a galeria até o item fornecido.
6.  O elemento `.thumbnails` é preenchido usando `Array.prototype.map()` e `Array.prototype.join()`. Cada miniatura recebe um atributo `data-id` com o índice da imagem.
7.  Um manipulador para o evento `'click'` é registrado em cada miniatura usando `Document.querySelectorAll()`, `Array.prototype.forEach()`, `EventTarget.addEventListener()` e a função `scrollToElement`.
8.  Um manipulador para o evento `'scroll'` é registrado usando `Document.querySelector()` e `EventTarget.addEventListener()`. Os elementos `.thumbnails` e `.scrollbar` são atualizados para corresponder à posição atual da rolagem usando a função `scrollThumb`.

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

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
