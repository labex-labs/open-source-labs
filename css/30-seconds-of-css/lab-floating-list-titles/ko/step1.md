# 플로팅 섹션 제목이 있는 목록

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

각 섹션에 대해 플로팅 제목이 있는 목록을 만들려면 다음 단계를 따르세요.

1. 수직 오버플로우를 허용하기 위해 목록 컨테이너에 `overflow-y: auto`를 적용합니다.
2. 내부 컨테이너 (`<dl>`) 에 `display: grid`를 사용하여 두 개의 열이 있는 레이아웃을 만듭니다.
3. 제목 (`<dt>`) 을 `grid-column: 1`로, 콘텐츠 (`<dd>`) 를 `grid-column: 2`로 설정합니다.
4. 마지막으로, 플로팅 효과를 만들기 위해 제목에 `position: sticky` 및 `top: 0.5rem`을 적용합니다.

다음은 HTML 코드입니다.

```html
<div class="container">
  <div class="floating-stack">
    <dl>
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
</div>
```

다음은 CSS 코드입니다.

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
