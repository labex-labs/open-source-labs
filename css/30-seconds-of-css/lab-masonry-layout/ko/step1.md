# 메이슨리 레이아웃 (Masonry Layout)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

메이슨리 스타일 레이아웃을 만들려면 `.masonry-container`를 메인 컨테이너로 사용하고, `.masonry-brick` 요소가 배치될 내부 컨테이너로 `.masonry-columns`를 추가합니다. 레이아웃은 서로 겹쳐져 완벽한 핏을 형성하는 "벽돌 (bricks)"로 구성됩니다. 수직 레이아웃의 경우 `width`, 수평 레이아웃의 경우 `height`를 고정할 수 있습니다.

레이아웃이 제대로 흐르도록 하려면 `.masonry-brick` 요소에 `display: block`을 적용합니다. `:first-child` 의사 요소 선택자를 사용하여 첫 번째 요소의 위치를 고려하여 다른 `margin`을 적용합니다.

더 큰 유연성과 반응성을 위해 CSS 변수와 미디어 쿼리를 사용합니다. `.masonry-container`는 열 수와 간격에 대한 CSS 변수를 가지고 있습니다. 열의 수는 다양한 화면 크기에 대해 다른 열 수와 너비를 지정하는 미디어 쿼리에 의해 제어됩니다.

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

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
