# 팝아웃 메뉴

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

마우스 오버/포커스 시 대화형 팝아웃 메뉴를 표시하려면 다음 단계를 따르세요.

1. CSS 에서 `left: 100%`를 사용하여 팝아웃 메뉴를 부모 요소의 오른쪽에 배치합니다.
2. 전환 (transition) 을 적용할 수 있도록, 처음에는 `display: none` 대신 `visibility: hidden`을 사용하여 팝아웃 메뉴를 숨깁니다.
3. 마우스 오버/포커스 시 팝아웃 메뉴를 표시하기 위해 부모 요소에 `:hover`, `:focus`, 및 `:focus-within` 의사 클래스 선택자를 적용합니다.
4. 다음 HTML 및 CSS 코드를 사용합니다.

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover > .popout-menu,
.reference:focus > .popout-menu,
.reference:focus-within > .popout-menu {
  visibility: visible;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
