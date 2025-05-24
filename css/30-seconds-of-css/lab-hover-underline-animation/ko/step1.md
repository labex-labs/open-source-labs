# 호버 언더라인 애니메이션

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

사용자가 텍스트 위로 마우스를 가져갈 때 애니메이션 언더라인 효과를 만들려면 다음 단계를 따르세요.

1. `display: inline-block`을 사용하여 언더라인이 텍스트 내용의 너비만큼만 span 되도록 합니다.
2. `::after` 가상 요소 (pseudo-element) 를 `width: 100%` 및 `position: absolute`와 함께 사용하여 콘텐츠 아래에 배치합니다.
3. `transform: scaleX(0)`을 사용하여 초기에는 가상 요소를 숨깁니다.
4. `:hover` 가상 클래스 선택자 (pseudo-class selector) 를 사용하여 `transform: scaleX(1)`을 적용하고 호버 시 가상 요소를 표시합니다.
5. `transform-origin: left` 및 적절한 `transition`을 사용하여 `transform`을 애니메이션화합니다.
6. `transform-origin` 속성을 제거하여 변환이 요소의 중앙에서 시작되도록 합니다.

다음은 텍스트 요소에 효과를 적용하는 HTML 코드 예시입니다.

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

다음은 해당 CSS 코드입니다.

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
