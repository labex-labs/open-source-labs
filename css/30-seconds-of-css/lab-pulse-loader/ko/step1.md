# 펄스 로더 (Pulse Loader)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

`animation-delay` 속성을 사용하여 펄스 효과 로더 애니메이션을 만들려면 다음 단계를 따르세요.

1. `@keyframes`를 사용하여 두 개의 `<div>` 요소에 대한 애니메이션을 정의합니다. 두 요소 모두 시작점 (`0%`) 에서 `width` 또는 `height`가 없고 중앙에 위치하도록 설정합니다. 종료점 (`100%`) 에서는 두 요소 모두 `width`와 `height`가 증가하지만 `position`을 `0`으로 재설정합니다.
2. `opacity`를 사용하여 애니메이션 시 `1`에서 `0`으로 전환하여 `<div>` 요소가 확장되면서 사라지는 효과를 줍니다.
3. 부모 컨테이너인 `.ripple-loader`에 미리 정의된 `width`와 `height`를 설정합니다. 자식 요소를 배치하기 위해 `position: relative`를 사용합니다.
4. 두 번째 `<div>` 요소에 `animation-delay`를 사용하여 각 요소가 서로 다른 시간에 애니메이션을 시작하도록 합니다.

다음은 이를 구현하기 위한 HTML 및 CSS 코드입니다.

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
