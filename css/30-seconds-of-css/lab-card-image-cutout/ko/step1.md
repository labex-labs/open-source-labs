# 이미지 컷아웃이 있는 카드

`index.html` 및 `style.css` 파일은 이미 VM 에 제공되었습니다.

이미지 컷아웃이 있는 카드를 만들려면 다음 단계를 따르세요.

1. `background` 속성을 사용하여 `.container` 요소에 색상 배경을 추가합니다.
2. `.card` 요소를 만들고 원하는 이미지와 기타 콘텐츠가 포함된 `figure` 요소를 그 안에 추가합니다.
3. `::before` 가상 요소 (pseudo-element) 를 사용하여 `figure` 요소 주위에 `border`를 추가합니다. 테두리 색상을 `.container` 요소의 `background` 색상과 일치시켜 `.card`에서 컷아웃 효과를 만듭니다.

다음은 카드의 HTML 코드 예시입니다.

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

다음은 해당 CSS 코드입니다.

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card .content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
