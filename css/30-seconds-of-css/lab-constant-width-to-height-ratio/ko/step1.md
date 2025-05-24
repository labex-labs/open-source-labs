# 고정된 너비 대 높이 비율

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

이 코드 조각은 가변적인 `width`를 가진 요소가 비례적인 `height` 값을 유지하도록 보장합니다. 이를 위해 `::before` 가상 요소에 `padding-top`을 적용하여 요소의 `height`가 `width`의 백분율과 같도록 만듭니다. `height` 대 `width`의 비율은 필요에 따라 변경할 수 있습니다. 예를 들어, `padding-top`이 `100%`이면 1:1 비율의 반응형 사각형이 생성됩니다. 이 코드를 사용하려면 다음 HTML 코드를 추가하십시오.

```html
<div class="constant-width-to-height-ratio"></div>
```

그런 다음 다음 CSS 코드를 추가하십시오.

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
