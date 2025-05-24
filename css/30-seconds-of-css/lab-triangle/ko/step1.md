# 삼각형 (Triangle)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

순수 CSS 로 삼각형 모양을 만들려면 다음 단계를 따르세요:

1. 동일한 `border-width` (`20px`) 를 가진 세 개의 테두리 (border) 를 사용하여 삼각형 모양을 만듭니다.
2. 삼각형이 가리키는 반대쪽의 `border-color`를 원하는 색상으로 설정합니다. 인접한 테두리는 `border-color`를 `transparent`로 설정해야 합니다.
3. 삼각형의 크기를 조정하려면 `border-width` 값을 변경합니다.

다음은 코드 예시입니다:

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
