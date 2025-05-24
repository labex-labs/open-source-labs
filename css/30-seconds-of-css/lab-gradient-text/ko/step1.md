# 그라데이션 텍스트

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

텍스트에 그라데이션 색상을 적용하려면 CSS 속성을 사용할 수 있습니다. 먼저, `linear-gradient()` 값을 사용하여 `background` 속성을 사용하여 텍스트 요소에 그라데이션 배경을 지정합니다. 그런 다음, `webkit-text-fill-color: transparent`를 사용하여 텍스트를 투명한 색상으로 채웁니다. 마지막으로, `webkit-background-clip: text`를 사용하여 텍스트로 배경을 클리핑하고 텍스트를 그라데이션 배경으로 색상을 채웁니다. 다음은 예시 코드 조각입니다.

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
