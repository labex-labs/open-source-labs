# 버튼 성장 애니메이션

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

호버 시 성장 애니메이션을 만들려면 적절한 `transition`을 사용하여 요소의 변경 사항을 애니메이션화할 수 있습니다. `:hover` 의사 클래스를 사용하여 `transform` 속성을 `scale(1.1)`로 변경합니다. 이렇게 하면 사용자가 버튼 위로 마우스를 가져갈 때 요소가 커집니다.

다음은 사용할 수 있는 코드 스니펫 예시입니다.

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
