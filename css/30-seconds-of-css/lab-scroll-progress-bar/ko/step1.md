# 스크롤 진행률 표시줄

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

웹 페이지의 스크롤 백분율을 표시하는 진행률 표시줄을 만들려면 다음 단계를 따르세요.

1. HTML 코드에 `id`가 "scroll-progress"인 `div` 요소를 추가합니다.
2. CSS 코드에서 요소의 `position`을 `fixed`로, `top`을 `0`으로, `width`를 `0%`로, `height`를 `4px`로, `background` 색상을 `#7983ff`로 설정합니다.
3. `z-index` 값을 큰 숫자로 설정하여 진행률 표시줄이 페이지 상단에, 그리고 모든 콘텐츠 위에 배치되도록 합니다.
4. JavaScript 코드에서 `document.getElementById()` 메서드를 사용하여 `scroll-progress` 요소를 선택합니다.
5. `document.documentElement.scrollHeight - document.documentElement.clientHeight` 공식을 사용하여 웹 페이지의 높이를 계산합니다.
6. `scroll` 이벤트를 수신하는 `window` 객체에 이벤트 리스너를 추가합니다.
7. 이벤트 리스너 함수에서 `(scrollTop / height) * 100` 공식을 사용하여 문서의 스크롤 백분율을 계산합니다.
8. `style` 속성을 사용하여 `scroll-progress` 요소의 `width`를 스크롤 백분율로 설정합니다.

다음은 코드입니다.

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
