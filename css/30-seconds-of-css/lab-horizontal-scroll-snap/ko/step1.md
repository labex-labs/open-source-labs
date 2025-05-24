# 수평 스크롤 스냅 (Horizontal Scroll Snap)

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

스크롤 시 요소에 스냅되는 수평 스크롤 가능 컨테이너를 만들려면 다음 단계를 따르세요.

1. `display: grid` 및 `grid-auto-flow: column`을 사용하여 수평 레이아웃을 만듭니다.
2. `scroll-snap-type: x mandatory` 및 `overscroll-behavior-x: contain`을 사용하여 수평 스크롤에 스냅 효과를 만듭니다.
3. `scroll-snap-align`을 `start`, `stop` 또는 `center`로 변경하여 스냅 정렬을 조정합니다.

다음은 사용할 수 있는 HTML 및 CSS 코드 예시입니다.

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
