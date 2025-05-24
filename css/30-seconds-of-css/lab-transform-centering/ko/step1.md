# 변환 (Transform) 을 이용한 중앙 정렬

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

CSS 변환을 사용하여 자식 요소를 부모 요소 내에서 수직 및 수평으로 중앙 정렬하려면 다음 단계를 따르세요.

1. 부모 요소의 `position` 속성을 `relative`로 설정하고 자식 요소의 `position` 속성을 `absolute`로 설정하여 부모를 기준으로 위치를 지정합니다.
2. `left: 50%` 및 `top: 50%`을 사용하여 자식 요소를 부모 요소의 왼쪽 및 상단 가장자리에서 50% 만큼 오프셋합니다.
3. `transform: translate(-50%, -50%)`을 사용하여 위치를 상쇄 (negate) 하여 수직 및 수평으로 모두 중앙 정렬되도록 합니다.
4. 부모 요소의 고정된 `height`와 `width`는 시연 목적으로만 사용됩니다.

다음은 HTML 코드 예시입니다.

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

다음은 해당 CSS 코드입니다.

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
