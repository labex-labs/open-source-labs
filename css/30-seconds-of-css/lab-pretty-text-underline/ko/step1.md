# 예쁜 텍스트 밑줄

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

디센더가 밑줄을 자르는 것을 방지하려면, `text-shadow`에 네 개의 값을 사용하여 디센더가 밑줄과 만나는 선을 덮는 두꺼운 그림자를 만듭니다. `text-shadow`의 색상이 `background` 색상과 일치하는지 확인하고, 더 큰 글꼴의 경우 `px` 값을 조정합니다. `linear-gradient()`와 `currentColor`를 사용하여 `background-image`로 실제 밑줄을 만듭니다. `background-position`, `background-repeat`, `background-size`를 설정하여 그라데이션을 올바른 위치에 배치합니다. `::selection` 의사 클래스 선택자를 사용하여 텍스트 그림자가 텍스트 선택을 방해하지 않도록 합니다. 이 효과는 기본적으로 `text-decoration-skip-ink: auto`로 구현되지만, 밑줄에 대한 제어력이 더 적습니다.

다음은 코드 스니펫 예시입니다.

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
