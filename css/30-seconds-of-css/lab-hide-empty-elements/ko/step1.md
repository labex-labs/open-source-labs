# 빈 요소 숨기기

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

내용이 없는 요소를 숨기려면 `:empty` 가상 클래스를 사용하십시오. 예를 들어, 다음과 같은 HTML 코드가 있는 경우:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

다음 CSS 코드를 사용하여 내용이 없는 button 요소를 숨길 수 있습니다:

```css
p:empty {
  display: none;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
