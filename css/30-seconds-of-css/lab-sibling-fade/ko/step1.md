# Sibling Fade (형제 페이드)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

호버된 항목의 형제 요소를 흐리게 하려면 다음 단계를 따르세요:

1. `transition` 속성을 사용하여 `opacity` 변경을 애니메이션화합니다.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. `:hover` 및 `:not` 의사 클래스 선택자를 사용하여 마우스가 위에 있지 않은 모든 요소의 `opacity`를 `0.5`로 변경합니다.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

다음은 HTML 코드 예시입니다:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
