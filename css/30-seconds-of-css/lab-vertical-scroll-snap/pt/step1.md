# Scroll Snap Vertical

`index.html` e `style.css` já foram fornecidos na VM.

Este código cria um contêiner rolável que se ajusta (snap) aos elementos durante a rolagem. Para alcançar este efeito, as seguintes etapas são tomadas:

1. `display: grid` e `grid-auto-flow: row` são usados para criar um layout vertical.
2. `scroll-snap-type: y mandatory` e `overscroll-behavior-y: contain` são usados para criar o efeito de ajuste (snap) na rolagem vertical.
3. `scroll-snap-align` com `start`, `stop` ou `center` pode ser usado para alterar o alinhamento do ajuste (snap).

Aqui está o código HTML e CSS:

```html
<div class="vertical-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640" /></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640" /></a>
</div>
```

```css
.vertical-snap {
  margin: 0 auto;
  display: grid;
  grid-auto-flow: row;
  gap: 1rem;
  width: calc(180px + 1rem);
  padding: 1rem;
  height: 480px;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-snap-type: y mandatory;
}

.vertical-snap > a {
  scroll-snap-align: center;
}

.vertical-snap img {
  width: 180px;
  object-fit: contain;
  border-radius: 1rem;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
