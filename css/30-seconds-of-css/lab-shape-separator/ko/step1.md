# 모양 분리자

`index.html` 및 `style.css` 파일은 이미 VM 에 제공되었습니다.

SVG 모양을 사용하여 두 개의 서로 다른 블록 사이에 분리자 요소를 만들려면 다음 단계를 따르세요.

1. `::after` 의사 요소 (pseudo-element) 를 사용합니다.
2. `background-image` 속성을 사용하여 데이터 URI 를 통해 SVG 모양 (24x12 삼각형) 을 추가합니다. 배경 이미지는 기본적으로 반복되며 의사 요소의 전체 영역을 덮습니다.
3. 부모 요소의 `background` 속성을 사용하여 분리자에 원하는 색상을 설정합니다.

다음 HTML 코드를 사용하세요:

```html
<div class="shape-separator"></div>
```

그리고 다음 CSS 규칙을 적용합니다:

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
