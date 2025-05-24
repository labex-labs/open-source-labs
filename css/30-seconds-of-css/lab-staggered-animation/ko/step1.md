# 계단식 애니메이션 (Staggered Animation)

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

이 코드는 목록 요소에 대한 계단식 애니메이션을 생성합니다. 이를 위해 다음을 수행합니다.

1. `opacity: 0` 및 `transform: translateX(100%)`을 설정하여 목록 요소를 투명하게 만들고 오른쪽으로 완전히 이동합니다.
2. `transition-delay`를 제외하고 목록 요소에 대해 동일한 `transition` 속성을 지정합니다.
3. 인라인 스타일을 사용하여 각 목록 요소에 대한 `--i` 값을 지정합니다. 이 값은 계단식 효과를 만들기 위해 `transition-delay`에 사용됩니다.
4. 체크박스에 `:checked` 의사 클래스 선택자를 사용하여 목록 요소를 스타일링합니다. 나타나고 보기 좋게 슬라이드되도록 하려면 `opacity`를 `1`로, `transform`을 `translateX(0)`으로 설정합니다.

다음은 이 효과를 얻기 위한 HTML 및 CSS 코드입니다.

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
