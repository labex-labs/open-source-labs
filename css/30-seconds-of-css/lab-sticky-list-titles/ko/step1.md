# 고정 섹션 제목이 있는 목록

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

각 섹션에 고정 제목이 있는 목록을 만들려면 다음 단계를 따르세요.

1. `overflow-y: auto`를 사용하여 목록 컨테이너 (`<dl>`) 가 세로로 넘치도록 허용합니다.
2. 제목 (`<dt>`) 의 `position`을 `sticky`로 설정하고 `top: 0`을 적용하여 컨테이너 상단에 고정합니다.
3. 다음 HTML 및 CSS 코드를 사용합니다.

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>Algeria</dd>
    <dd>Angola</dd>

    <dt>B</dt>
    <dd>Benin</dd>
    <dd>Botswana</dd>
    <dd>Burkina Faso</dd>
    <dd>Burundi</dd>

    <dt>C</dt>
    <dd>Cabo Verde</dd>
    <dd>Cameroon</dd>
    <dd>Central African Republic</dd>
    <dd>Chad</dd>
    <dd>Comoros</dd>
    <dd>Congo, Democratic Republic of the</dd>
    <dd>Congo, Republic of the</dd>
    <dd>Cote d'Ivoire</dd>

    <dt>D</dt>
    <dd>Djibouti</dd>

    <dt>E</dt>
    <dd>Egypt</dd>
    <dd>Equatorial Guinea</dd>
    <dd>Eritrea</dd>
    <dd>Eswatini (formerly Swaziland)</dd>
    <dd>Ethiopia</dd>
  </dl>
</div>
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
