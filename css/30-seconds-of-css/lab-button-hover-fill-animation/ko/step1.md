# 버튼 채우기 애니메이션

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

호버 시 채우기 애니메이션을 만들려면 `color` (색상) 및 `background` (배경) 속성을 설정하고 적절한 `transition` (전환) 을 적용하여 변경 사항을 애니메이션화할 수 있습니다. 호버 시 애니메이션을 트리거하려면 `:hover` 의사 클래스를 사용하여 요소의 `background` (배경) 및 `color` (색상) 속성을 변경합니다. 다음은 코드 스니펫 예시입니다.

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
