# 그리드 중앙 정렬 (Grid Centering)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

부모 요소 내에서 자식 요소를 수평 및 수직으로 모두 중앙 정렬하려면 다음 단계를 따르세요.

1. `display: grid`를 사용하여 그리드 레이아웃을 생성합니다.
2. `justify-content: center`를 사용하여 자식을 수평으로 중앙 정렬합니다.
3. `align-items: center`를 사용하여 자식을 수직으로 중앙 정렬합니다.

다음은 HTML 구조의 예입니다.

```html
<div class="parent">
  <div class="child">Centered content.</div>
</div>
```

그리고 해당 CSS 는 다음과 같습니다.

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
