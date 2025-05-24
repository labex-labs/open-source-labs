# 로드 실패 시 이미지 대체 (Fallback)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

이미지 로딩에 실패하면 사용자에게 오류 메시지를 표시합니다. 이를 위해 `img` 요소에 텍스트 컨테이너처럼 스타일을 적용하여 display 를 block 으로, width 를 100% 로 설정합니다. `::before` 및 `::after` 가상 요소 (pseudo-elements) 를 사용하여 각각 오류 메시지와 이미지 URL 을 표시합니다. 이러한 요소는 이미지가 로드에 실패한 경우에만 표시됩니다.

다음은 코드 스니펫 예시입니다.

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
