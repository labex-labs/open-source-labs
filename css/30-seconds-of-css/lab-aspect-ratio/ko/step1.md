# 종횡비 (Aspect Ratio)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

이 코드는 CSS 사용자 정의 속성 (custom property) 과 `calc()` 함수를 사용하여 특정 종횡비를 가진 반응형 컨테이너를 생성합니다. 다음 단계를 따라 이를 구현하십시오.

1. CSS 사용자 정의 속성 `--aspect-ratio`를 사용하여 원하는 종횡비를 정의합니다.
2. 컨테이너 요소의 `position` 속성을 `relative`로 설정하고 `height` 속성을 `0`으로 설정합니다.
3. `calc()` 함수와 `--aspect-ratio` 사용자 정의 속성을 사용하여 컨테이너 요소의 높이를 계산하고, 이를 `padding-bottom` 속성으로 설정합니다.
4. 컨테이너 요소의 직접적인 자식 요소의 `position`을 `absolute`, `top: 0`, `left: 0`, `width: 100%`, `height: 100%`로 설정합니다.
5. 자식 요소의 `object-fit` 속성을 `cover`로 설정하여 자식 요소의 종횡비를 유지합니다.

다음 HTML 및 CSS 코드를 사용하여 컨테이너를 생성하십시오.

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
