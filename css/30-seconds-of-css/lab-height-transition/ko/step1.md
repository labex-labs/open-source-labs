# 높이 전환

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

이 코드 조각은 다음 단계를 수행하여 요소의 높이를 알 수 없을 때 요소의 높이를 `0`에서 `auto`로 전환합니다.

- `transition` 속성을 사용하여 `max-height`에 대한 변경 사항이 `0.3s` 동안 전환되도록 지정합니다.
- `overflow` 속성을 `hidden`으로 설정하여 숨겨진 요소의 내용이 컨테이너를 넘치지 않도록 합니다.
- `max-height` 속성을 사용하여 초기 높이를 `0`으로 지정합니다.
- `:hover` 의사 클래스를 사용하여 `max-height`를 JavaScript 에서 설정한 `--max-height` 변수의 값으로 변경합니다.
- `Element.scrollHeight` 속성 및 `CSSStyleDeclaration.setProperty()` 메서드를 사용하여 `--max-height`의 값을 요소의 현재 높이로 설정합니다.
- **참고:** 이 접근 방식은 각 애니메이션 프레임에서 리플로우 (reflow) 를 발생시키므로, 전환되는 요소 아래에 많은 수의 요소가 있는 경우 지연이 발생할 수 있습니다.

```html
<div class="trigger">
  Hover over me to see a height transition.
  <div class="el">Additional content</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
