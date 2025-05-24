# 텍스트 잘라내기 (Truncate Text)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

한 줄보다 긴 텍스트를 잘라내고 끝에 줄임표를 추가하려면 다음 CSS 속성을 사용하십시오.

- `overflow: hidden`: 텍스트가 치수를 초과하는 것을 방지합니다.
- `white-space: nowrap`: 텍스트가 높이에서 한 줄을 초과하는 것을 방지합니다.
- `text-overflow: ellipsis`: 텍스트가 치수를 초과하는 경우 줄임표를 추가합니다.
- 줄임표를 표시할 시점을 알기 위해 요소의 고정된 `width`를 지정합니다.

이 방법은 단일 행 요소에만 적용됩니다. 예를 들어:

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
