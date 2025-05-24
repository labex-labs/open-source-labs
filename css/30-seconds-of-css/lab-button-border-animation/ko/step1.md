# 버튼 테두리 애니메이션

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

호버 시 테두리 애니메이션을 만들려면 `::before` 및 `::after` 가상 요소 (pseudo-elements) 를 사용하여 너비가 `24px`이고 상자 위와 아래에 위치한 두 개의 상자를 생성할 수 있습니다. 그런 다음 `:hover` 가상 클래스 (pseudo-class) 를 적용하여 호버 시 해당 요소의 `width`를 `100%`로 늘리고 `transition`을 사용하여 전환을 애니메이션화합니다.

다음은 예시 코드 조각입니다.

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
