# 동적 그림자

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

요소의 색상을 기반으로 하는 그림자를 만들려면 다음 단계를 따르세요.

1. `::after` 가상 요소에 `position: absolute`를 사용하고 `width` 및 `height`를 `100%`로 설정하여 부모 요소의 사용 가능한 공간을 채웁니다.

2. `background: inherit`를 사용하여 부모 요소의 `background`를 상속합니다.

3. `top`을 사용하여 가상 요소를 약간 오프셋합니다. 그런 다음, `filter: blur()`를 사용하여 그림자를 만들고 `opacity`를 설정하여 반투명하게 만듭니다.

4. `z-index: -1`을 설정하여 가상 요소를 부모 요소 뒤에 배치합니다. 부모 요소에는 `z-index: 1`을 설정합니다.

다음은 HTML 및 CSS 코드의 예입니다.

```html
<div class="dynamic-shadow"></div>
```

```css
.dynamic-shadow {
  position: relative;
  width: 10rem;
  height: 10rem;
  background: linear-gradient(75deg, #6d78ff, #00ffb8);
  z-index: 1;
}

.dynamic-shadow::after {
  content: "";
  width: 100%;
  height: 100%;
  position: absolute;
  background: inherit;
  top: 0.5rem;
  filter: blur(0.4rem);
  opacity: 0.7;
  z-index: -1;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
