# 스크롤바 숨기기

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

스크롤바를 숨기면서 요소가 스크롤 가능하도록 하려면 다음 단계를 따르세요.

- `overflow: auto`를 사용하여 요소에서 스크롤을 활성화합니다.
- Firefox 에서 스크롤바를 숨기려면 `scrollbar-width: none`을 사용합니다.
- WebKit 브라우저 (Chrome, Edge, Safari 등) 에서 스크롤바를 숨기려면 `::-webkit-scrollbar` 의사 요소에 `display: none`을 사용합니다.

다음은 구현 예시입니다.

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
