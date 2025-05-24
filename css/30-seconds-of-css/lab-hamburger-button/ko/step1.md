# 햄버거 버튼 (Hamburger Button)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

마우스를 올렸을 때 (hover) 십자 버튼으로 전환되는 햄버거 메뉴를 만들려면 다음 단계를 따르세요:

1. 상단, 하단, 중간 막대를 포함하는 `.hamburger-menu` 컨테이너 `div`를 사용합니다.
2. 컨테이너를 `display: flex`로 설정하고 `flex-flow: column wrap`을 사용합니다.
3. `justify-content: space-between`을 사용하여 막대 사이에 간격을 추가합니다.
4. `transform: rotate()`를 사용하여 상단 및 하단 막대를 45 도 회전시키고, 마우스를 올렸을 때 중간 막대를 `opacity: 0`으로 페이드 처리합니다.
5. 막대가 왼쪽 지점을 중심으로 회전하도록 `transform-origin: left`를 사용합니다.

다음은 해당 HTML 코드입니다:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

다음은 CSS 코드입니다:

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu .bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover .top {
  transform: rotate(45deg);
}

.hamburger-menu:hover .middle {
  opacity: 0;
}

.hamburger-menu:hover .bottom {
  transform: rotate(-45deg);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
