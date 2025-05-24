# 네비게이션 목록 항목 Hover 및 Focus 효과

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

네비게이션 항목에 대한 사용자 정의 hover 및 focus 효과를 생성하려면 다음과 같이 CSS 변환 (CSS transformations) 을 사용하십시오.

1. hover 효과를 생성하기 위해 목록 항목 앵커 (list item anchor) 에서 `::before` 가상 요소 (pseudo-element) 를 사용합니다. `transform: scale(0)`을 사용하여 숨깁니다.
2. `:hover` 및 `:focus` 가상 클래스 선택자 (pseudo-class selectors) 를 사용하여 가상 요소를 `transform: scale(1)`로 전환하고 색상 배경을 표시합니다.
3. `z-index`를 사용하여 가상 요소가 앵커 요소를 덮는 것을 방지합니다.

다음 HTML 코드를 네비게이션 메뉴에 사용할 수 있습니다.

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

그리고 다음 CSS 규칙을 적용합니다.

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
