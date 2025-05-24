# 화면 밖 (Offscreen)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

이 기술은 DOM 에서 요소를 완전히 숨기면서도 접근 가능하게 만듭니다. 이를 위해 다음 단계를 따를 수 있습니다.

- 모든 테두리와 패딩을 제거하고 요소의 오버플로우 (overflow) 를 숨깁니다.
- `clip`을 사용하여 요소의 어떤 부분도 표시되지 않도록 합니다.
- 요소의 `height`와 `width`를 `1px`로 설정하고 `margin: -1px`를 사용하여 음수로 만듭니다.
- `position: absolute`를 사용하여 요소가 DOM 에서 공간을 차지하지 않도록 합니다.
- 이 기술은 접근성과 레이아웃 친화성 측면에서 `display: none` (스크린 리더에서 읽을 수 없음) 및 `visibility: hidden` (DOM 에서 물리적 공간을 차지함) 의 더 나은 대안입니다.

HTML 과 CSS 에서 이 기술을 사용하는 방법의 예는 다음과 같습니다.

```html
<a class="button" href="https://google.com">
  Learn More <span class="offscreen">about pants</span>
</a>
```

```css
.offscreen {
  border: 0;
  clip: rect(0 0 0 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
