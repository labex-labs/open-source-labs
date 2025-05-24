# 선택 비활성화

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

요소의 콘텐츠를 선택할 수 없도록 하려면 CSS 속성 `user-select: none`을 선택기에 추가하십시오. 그러나 이 방법은 사용자가 콘텐츠를 복사하는 것을 완전히 안전하게 방지하지는 못합니다.

예시:

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
