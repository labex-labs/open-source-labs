# 도넛 스피너 (Donut Spinner)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

콘텐츠 로딩을 나타내기 위해 전체 요소에 반투명한 `border`를 사용하여 도넛 스피너를 만듭니다. 도넛의 로딩 표시기로 사용할 한쪽 면을 제외합니다. 그런 다음, `transform: rotate()`를 사용하여 요소를 회전시키는 적절한 애니메이션을 정의하고 사용합니다. 다음은 HTML 및 CSS 의 예시 코드입니다.

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
