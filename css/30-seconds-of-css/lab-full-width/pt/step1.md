# Imagem de Largura Total

> Você pode escrever o código em `index.html` e `style.css`..

Cria uma imagem de largura total.

- Use `left: 50%` e `right: 50%` para posicionar a imagem no meio do elemento pai.
- Use `margin-left: -50vw` e `margin-right: -50vw` para compensar a imagem em ambos os lados em relação ao tamanho da viewport (área de visualização).
- Use `width: 100vw` e `max-width: 100vw` para dimensionar a imagem em relação à viewport.

```html
<main>
  <h4>Lorem ipsum dolor sit amet</h4>
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris molestie
    lobortis sapien, sit amet iaculis est interdum tincidunt. Nunc egestas nibh
    ut metus elementum consequat. Integer elit orci, rhoncus efficitur lectus
    eu, faucibus interdum felis.
  </p>
  <p>
    <img class="full-width" src="https://picsum.photos/id/257/2560/1440.jpg" />
  </p>
  <p>
    Orci varius natoque penatibus et magnis dis parturient montes, nascetur
    ridiculus mus. Nullam pretium lectus sed ex efficitur, ac varius sapien
    gravida. Sed facilisis elit quis sem sollicitudin, ut aliquam neque
    eleifend. Maecenas sagittis neque sapien, ac tempus nulla tempus nec.
    Curabitur tellus est, convallis id dolor ut, porta hendrerit quam.
  </p>
</main>
```

```css
main {
  margin: 0 auto;
  max-width: 640px;
}

img {
  height: auto;
  max-width: 100%;
}

.full-width {
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  max-width: 100vw;
  width: 100vw;
}
```
