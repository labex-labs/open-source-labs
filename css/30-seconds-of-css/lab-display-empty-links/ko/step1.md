# 텍스트가 없는 링크 스타일 지정

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

텍스트가 없는 링크의 URL 을 표시하려면, `:empty` 의사 클래스를 사용하여 해당 링크를 선택하고, `:not` 의사 클래스를 사용하여 텍스트가 있는 링크를 제외하며, `content` 속성을 `attr()` 함수와 함께 사용하여 `::before` 의사 요소에 링크 URL 을 표시할 수 있습니다. 다음은 예시 코드 조각입니다.

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
