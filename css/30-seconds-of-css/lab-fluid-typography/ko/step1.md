# 유동적인 타이포그래피 (Fluid Typography)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

뷰포트 너비를 기반으로 크기가 조정되는 텍스트를 만들려면 CSS 를 사용할 수 있습니다. 이를 수행하는 한 가지 방법은 `clamp()` 함수를 사용하여 최소 및 최대 글꼴 크기를 설정하는 것입니다. 또 다른 방법은 공식을 사용하여 글꼴 크기에 대한 반응형 값을 계산하는 것입니다. 다음은 `fluid-type` 클래스가 있는 HTML 요소의 예입니다.

```html
<p class="fluid-type">Hello World!</p>
```

다음은 뷰포트 너비를 기반으로 글꼴 크기를 `1rem`과 `3rem` 사이에서 조정하도록 설정하는 해당 CSS 코드입니다.

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
