# Image en largeur totale

> Vous pouvez écrire le code dans `index.html` et `style.css`..

Crée une image en largeur totale.

- Utilisez `left: 50%` et `right: 50%` pour positionner l'image au milieu de l'élément parent.
- Utilisez `margin-left: -50vw` et `margin-right: -50vw` pour décaler l'image des deux côtés par rapport à la taille de la fenêtre d'affichage.
- Utilisez `width: 100vw` et `max-width: 100vw` pour dimensionner l'image par rapport à la fenêtre d'affichage.

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
