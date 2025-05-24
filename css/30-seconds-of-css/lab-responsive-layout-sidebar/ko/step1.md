# 사이드바가 있는 반응형 레이아웃

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

콘텐츠 영역과 사이드바가 있는 반응형 레이아웃을 만들려면, 부모 컨테이너에 `display: grid`를 사용하고, 두 번째 열 (사이드바) 에 `minmax()`를 사용하여 `150px`에서 `20%` 사이의 공간을 차지하도록 하며, 첫 번째 열 (메인 콘텐츠) 에 `1fr`을 사용하여 나머지 공간을 차지하도록 합니다. 다음은 HTML 및 CSS 코드의 예입니다.

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
