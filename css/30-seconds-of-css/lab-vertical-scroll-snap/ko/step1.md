# 수직 스크롤 스냅 (Vertical Scroll Snap)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

이 코드는 스크롤 시 요소에 스냅되는 스크롤 가능한 컨테이너를 생성합니다. 이 효과를 얻기 위해 다음 단계가 수행됩니다.

1. `display: grid`와 `grid-auto-flow: row`를 사용하여 수직 레이아웃을 생성합니다.
2. `scroll-snap-type: y mandatory`와 `overscroll-behavior-y: contain`을 사용하여 수직 스크롤에 스냅 효과를 생성합니다.
3. `scroll-snap-align`을 `start`, `stop` 또는 `center`와 함께 사용하여 스냅 정렬을 변경할 수 있습니다.

다음은 HTML 및 CSS 코드입니다.

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

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
