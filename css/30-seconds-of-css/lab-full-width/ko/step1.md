# 전체 너비 이미지

> `index.html`과 `style.css`에 코드를 작성할 수 있습니다.

전체 너비 이미지를 생성합니다.

- 부모 요소의 가운데에 이미지를 배치하려면 `left: 50%` 및 `right: 50%`를 사용합니다.
- 뷰포트 크기에 상대적으로 양쪽에서 이미지를 오프셋하려면 `margin-left: -50vw` 및 `margin-right: -50vw`를 사용합니다.
- 뷰포트에 상대적으로 이미지 크기를 조정하려면 `width: 100vw` 및 `max-width: 100vw`를 사용합니다.

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
