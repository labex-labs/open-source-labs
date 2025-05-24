# 원 (Circle)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

순수 CSS 를 사용하여 원형 모양을 만들려면, `border-radius: 50%` 속성을 사용하여 요소의 테두리를 곡선으로 만듭니다. 완벽한 원을 보장하기 위해 `width`와 `height`를 동일한 값으로 설정해야 합니다. 다른 값을 사용하면 타원이 생성됩니다. 다음은 예시 코드 조각입니다.

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
