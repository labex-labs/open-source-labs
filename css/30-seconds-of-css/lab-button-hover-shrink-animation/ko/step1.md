# 버튼 축소 애니메이션

`index.html` 및 `style.css` 파일은 이미 VM 에 제공되어 있습니다.

요소에 마우스 오버 시 축소 애니메이션을 만들려면, 적절한 `transition` 속성을 사용하여 변경 사항을 애니메이션화하고, `:hover` 의사 클래스를 사용하여 애니메이션을 트리거할 수 있습니다. 예를 들어, 사용자가 `button-shrink` 클래스를 가진 버튼 위로 마우스를 가져갈 때 버튼을 축소하려면 다음 CSS 를 추가할 수 있습니다.

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

이렇게 하면 변경 사항이 있을 때 버튼의 모든 속성에 전환 효과가 적용되고, 사용자가 마우스를 가져가면 버튼이 원래 크기의 80% 로 축소됩니다. 버튼에 대한 HTML 코드는 다음과 같습니다.

```html
<button class="button-shrink">Submit</button>
```

웹 서비스 (web service) 를 포트 8080 에서 실행하려면 오른쪽 하단 모서리에 있는 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
