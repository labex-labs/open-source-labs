# 텍스트 교체

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

텍스트 교체 애니메이션을 만들려면 다음 단계를 따르세요.

1. 교체될 텍스트를 담을 "alternating" 클래스와 "alternating-text" `id`를 가진 `<span>` 요소를 만듭니다.

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. CSS 에서 `<span>` 요소를 `display: none`으로 설정하여 사라지게 하는 `alternating-text`라는 애니메이션을 정의합니다.

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

3. JavaScript 에서 교체될 서로 다른 단어의 배열을 정의하고 첫 번째 단어를 사용하여 `<span>` 요소의 내용을 초기화합니다.

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. `EventTarget.addEventListener()`를 사용하여 `'animationiteration'` 이벤트에 대한 이벤트 리스너를 정의합니다. 이렇게 하면 애니메이션의 반복이 완료될 때마다 이벤트 핸들러가 실행됩니다. 이벤트 핸들러에서 `Element.innerHTML`을 사용하여 `<span>` 요소의 내용으로 `texts` 배열의 다음 요소를 표시합니다.

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
