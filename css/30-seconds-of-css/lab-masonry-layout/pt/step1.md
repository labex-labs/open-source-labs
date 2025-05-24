# _Masonry Layout_ (Layout em Alvenaria)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um _layout_ no estilo _masonry_, use `.masonry-container` como o contêiner principal e adicione `.masonry-columns` como um contêiner interno no qual os elementos `.masonry-brick` serão colocados. O _layout_ consiste em "tijolos" que se encaixam, formando um ajuste perfeito. A `width` (largura) para um _layout_ vertical e a `height` (altura) para um _layout_ horizontal podem ser fixas.

Para garantir que o _layout_ flua corretamente, aplique `display: block` aos elementos `.masonry-brick`. Use o seletor de pseudo-elemento `:first-child` para aplicar uma `margin` (margem) diferente para o primeiro elemento, a fim de considerar seu posicionamento.

Para maior flexibilidade e responsividade, use variáveis CSS e _media queries_ (consultas de mídia). O `.masonry-container` possui variáveis CSS para contagem de colunas e espaçamento. O número de colunas é controlado por _media queries_ que especificam diferentes contagens de colunas e larguras para diferentes tamanhos de tela.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
