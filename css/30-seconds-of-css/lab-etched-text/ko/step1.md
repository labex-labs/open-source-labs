# 에칭 텍스트 (Etched Text)

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

배경에 텍스트에 대한 "에칭 (etched)" 또는 조각 효과를 만들려면 다음 CSS 속성을 사용하십시오.

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

`text-shadow` 속성은 원점 위치에서 수평으로 `0px`, 수직으로 `2px` 떨어진 흰색 그림자를 생성합니다. 효과가 제대로 작동하려면 배경이 그림자보다 어두워야 합니다. 또한, 텍스트 색상은 배경에서 조각된 것처럼 보이도록 약간 흐리게 처리해야 합니다. 마지막으로, 효과를 얻으려면 단락과 같은 원하는 HTML 요소에 `etched-text` 클래스를 적용하십시오.

```html
<p class="etched-text">I appear etched into the background.</p>
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
