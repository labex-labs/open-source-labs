# 바운싱 로더 (Bouncing Loader)

`index.html`과 `style.css`는 이미 VM 에 제공되었습니다.

바운싱 로더 애니메이션을 생성하려면:

1. `opacity` 및 `transform` 속성을 사용하고, 더 나은 성능을 위해 `transform: translate3d()`를 사용하여 단일 축 변환을 수행하는 `@keyframes` 애니메이션을 정의합니다.
2. `.bouncing-loader` 클래스를 가진 부모 컨테이너를 생성합니다. 이 컨테이너는 `display: flex`와 `justify-content: center`를 사용하여 바운싱 원을 중앙에 배치합니다.
3. 바운싱 원을 위한 세 개의 `<div>` 요소에 동일한 `width`, `height`, 그리고 `border-radius: 50%`를 부여하여 원형으로 만듭니다.
4. 세 개의 바운싱 원 각각에 `bouncing-loader` 애니메이션을 적용합니다.
5. 각 원에 대해 서로 다른 `animation-delay`와 `animation-direction: alternate`를 사용하여 적절한 효과를 만듭니다.

다음은 HTML 코드입니다:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

다음은 CSS 코드입니다:

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
