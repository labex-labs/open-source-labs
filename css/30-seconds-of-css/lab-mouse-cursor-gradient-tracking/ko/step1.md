# 마우스 커서 그래디언트 추적

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

그래디언트가 마우스 커서를 따라가는 호버 효과를 만들려면 다음 단계를 따르세요.

1. 버튼에서 마우스의 위치를 추적하기 위해 두 개의 CSS 변수 `--x` 및 `--y`를 선언합니다.
2. 그래디언트의 치수를 수정하기 위해 CSS 변수 `--size`를 선언합니다.
3. `background: radial-gradient(circle closest-side, pink, transparent)`를 사용하여 올바른 위치에 그래디언트를 생성합니다.
4. `Document.querySelector()` 및 `EventTarget.addEventListener()`를 사용하여 `'mousemove'` 이벤트에 대한 핸들러를 등록합니다.
5. `Element.getBoundingClientRect()` 및 `CSSStyleDeclaration.setProperty()`를 사용하여 `--x` 및 `--y` CSS 변수의 값을 업데이트합니다.

다음은 버튼에 대한 HTML 코드입니다.

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

다음은 CSS 코드입니다.

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

마지막으로, 다음은 JavaScript 코드입니다.

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
