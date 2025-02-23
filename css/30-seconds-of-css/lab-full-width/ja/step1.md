# フル幅画像

> コードは `index.html` と `style.css` に記述できます。

フル幅の画像を作成します。

- `left: 50%` と `right: 50%` を使って、画像を親要素の中央に配置します。
- `margin-left: -50vw` と `margin-right: -50vw` を使って、画像をビューポートのサイズに対して両側にオフセットします。
- `width: 100vw` と `max-width: 100vw` を使って、画像をビューポートに対してサイズを設定します。

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
