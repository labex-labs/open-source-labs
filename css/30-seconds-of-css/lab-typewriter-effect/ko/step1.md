# 타자기 효과 (Typewriter Effect)

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

타자기 효과 애니메이션을 만들려면 다음 단계를 따르세요.

1. `typing` 및 `blink` 두 개의 애니메이션을 정의합니다. `typing`은 문자를 애니메이션하고, `blink`는 캐럿 (caret) 을 애니메이션합니다.
2. `::after` 가상 요소 (pseudo-element) 를 사용하여 컨테이너 요소에 캐럿을 추가합니다.
3. JavaScript 를 사용하여 내부 요소의 텍스트를 설정하고 문자 수를 포함하는 `--characters` 변수를 설정합니다. 이 변수는 텍스트를 애니메이션하는 데 사용됩니다.
4. 필요에 따라 `white-space: nowrap` 및 `overflow: hidden`을 사용하여 콘텐츠를 보이지 않게 합니다.

다음은 HTML 코드입니다.

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

다음은 CSS 코드입니다.

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

마지막으로, 다음은 JavaScript 코드입니다.

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
