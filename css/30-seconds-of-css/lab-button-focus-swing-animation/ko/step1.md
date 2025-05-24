# 버튼 스윙 애니메이션

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

포커스 시 스윙 애니메이션을 생성하려면, 요소의 변경 사항을 애니메이션화하기 위해 적절한 `transition`을 사용해야 합니다. 그런 다음, 요소에 `:focus` 의사 클래스 (pseudo-class) 를 적용하고 `transform`과 함께 `animation`을 사용하여 스윙하게 만듭니다. 마지막으로, 애니메이션을 한 번만 재생하도록 `animation-iteration-count`를 추가합니다. HTML 및 CSS 에서 이를 수행하는 방법의 예는 다음과 같습니다.

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
