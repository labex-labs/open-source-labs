# 호버 시 이미지 오버레이

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

호버 시 이미지 오버레이 효과를 표시하려면 다음 단계를 따르세요.

1. 오버레이의 상단 및 하단 바에 각각 `::before` 및 `::after` 가상 요소 (pseudo-elements) 를 사용합니다. 원하는 효과를 내기 위해 해당 요소의 `opacity`, `transform` 및 `transition`을 설정합니다.
2. 오버레이의 텍스트에 `<figcaption>`을 사용합니다. 텍스트를 이미지 중앙에 배치하기 위해 `display: flex`, `flex-direction: column` 및 `justify-content: center`를 설정합니다.
3. 모든 요소의 `opacity` 및 `transform`을 업데이트하고 오버레이를 표시하려면 `:hover` 가상 선택자 (pseudo-selector) 를 사용합니다.

사용할 HTML 코드는 다음과 같습니다.

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

사용할 CSS 코드는 다음과 같습니다.

```css
.hover-img {
  display: inline-block;
  margin: 8px;
  width: 100%;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  background-color: #000;
  color: #fff;
}

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
  transition: all 0.3s ease;
}

.hover-img::before {
  content: "";
  top: 0;
  bottom: auto;
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```

오른쪽 하단 모서리에서 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
