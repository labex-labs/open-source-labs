# 호버 시 추가 콘텐츠 표시

`index.html`과 `style.css`는 이미 VM 에 제공되었습니다.

호버 시 추가 콘텐츠를 표시하는 카드를 만들려면 다음 단계를 따르세요.

1. 카드의 세로 오버플로우 (overflow) 되는 요소를 숨기기 위해 `overflow: hidden`을 사용합니다.
2. 요소에 호버 (hover) 하거나, 포커스 (focus) 되거나, 하위 요소에 포커스가 있을 때 카드의 스타일을 변경하기 위해 `:hover` 및 `:focus-within` 의사 클래스 선택자를 사용합니다.
3. 호버/포커스 시 부드러운 전환 효과를 만들기 위해 `transition: 0.3s ease all`을 설정합니다.

다음은 카드에 대한 HTML 코드 예시입니다.

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

다음은 카드의 스타일을 지정하는 CSS 코드입니다.

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card .focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
