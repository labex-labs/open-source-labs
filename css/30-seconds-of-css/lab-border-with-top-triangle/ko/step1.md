# 상단 삼각형이 있는 테두리

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

상단에 삼각형이 있는 콘텐츠 컨테이너를 만들려면 다음 단계를 따르세요.

1. `::before` 및 `::after` 의사 요소 (pseudo-elements) 를 사용하여 두 개의 삼각형을 만듭니다.
2. 삼각형의 `border-color`와 `background-color`를 컨테이너와 일치하도록 설정합니다.
3. `::before` 삼각형의 `border-width`를 `::after` 삼각형보다 `1px` 더 넓게 설정하여 테두리 역할을 하도록 합니다.
4. `::after` 삼각형을 `::before` 삼각형의 오른쪽으로 `1px` 이동시켜 왼쪽 테두리가 표시되도록 합니다.

다음은 컨테이너에 대한 HTML 코드 예시입니다.

```html
<div class="container">Border with top triangle</div>
```

다음은 해당 CSS 코드입니다.

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
