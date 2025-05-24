# 사용자 정의 텍스트 선택

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

선택된 텍스트의 스타일을 수정하려면 `::selection` 의사 선택자 (pseudo-selector) 를 사용하십시오. 다음은 단락 요소 내의 텍스트를 선택하고 스타일을 지정하는 예제 코드 조각입니다.

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
