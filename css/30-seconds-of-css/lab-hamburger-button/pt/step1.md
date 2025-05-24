# Botão Hamburger

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um menu hamburger que se transforma em um botão de cruz ao passar o mouse, siga estes passos:

1. Use uma `div` container `.hamburger-menu` que contém as barras superior, inferior e do meio.
2. Defina o container para `display: flex` com `flex-flow: column wrap`.
3. Adicione distância entre as barras usando `justify-content: space-between`.
4. Use `transform: rotate()` para rotacionar as barras superior e inferior em 45 graus e `opacity: 0` para desaparecer a barra do meio ao passar o mouse.
5. Use `transform-origin: left` para que as barras girem em torno do ponto esquerdo.

Aqui está o código HTML correspondente:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

E aqui está o código CSS:

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu .bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover .top {
  transform: rotate(45deg);
}

.hamburger-menu:hover .middle {
  opacity: 0;
}

.hamburger-menu:hover .bottom {
  transform: rotate(-45deg);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
