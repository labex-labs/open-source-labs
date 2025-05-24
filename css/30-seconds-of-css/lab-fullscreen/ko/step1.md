# 전체 화면 (Fullscreen)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

전체 화면 모드에서 요소의 스타일을 지정하려면 `:fullscreen` CSS 의사 요소 선택자를 사용할 수 있습니다. `<button>` 및 `Element.requestFullscreen()`을 사용하여 미리 보기 목적으로 요소를 전체 화면으로 만드는 버튼을 만들 수도 있습니다. 다음은 예제 코드입니다.

```html
<div class="container">
  <p>
    <em>아래 버튼을 클릭하여 요소를 전체 화면 모드로 전환하세요. </em>
  </p>
  <div class="element" id="element">
    <p>전체 화면 모드에서 색상이 변경됩니다!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    전체 화면으로!
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* For Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* For modern browsers */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
