# 이미지 위에 마우스 오버 시 메뉴

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

사용자가 이미지 위에 마우스를 올렸을 때 메뉴 오버레이를 표시하려면, `<img>` 요소를 감싸는 `<figure>`와 메뉴 링크를 포함할 `<div>` 요소를 사용하십시오. 마우스 오버 시 이미지에 애니메이션을 적용하여 슬라이딩 효과를 만들려면 다음 CSS 속성을 적용하십시오.

- `opacity`
- `right`

`<div>`의 `left` 속성을 요소의 `width`의 음수 값으로 설정합니다. 부모 요소 위에 마우스를 올리면 메뉴가 슬라이드 인되도록 `0`으로 재설정합니다. 마지막으로, `<div>`에 `display: flex`, `flex-direction: column` 및 `justify-content: center`를 사용하여 메뉴 항목을 수직으로 가운데 정렬합니다.

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Home</a>
    <a href="#">Pricing</a>
    <a href="#">About</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
