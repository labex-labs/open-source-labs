# Overflow Scroll Gradient (오버플로우 스크롤 그라데이션)

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

넘치는 요소에 페이딩 그라데이션을 추가하고 스크롤해야 할 콘텐츠가 더 있음을 나타내려면 다음 단계를 따르세요.

1. `::after` 의사 요소를 사용하여 `transparent`에서 `white`로 (위에서 아래로) 페이드되는 `linear-gradient()`를 생성합니다.
2. `position: absolute`, `width`, 및 `height`를 사용하여 의사 요소를 부모 요소 내에서 위치시키고 크기를 지정합니다.
3. `pointer-events: none`을 사용하여 의사 요소를 마우스 이벤트에서 제외하여 그 뒤의 텍스트를 여전히 선택/상호 작용 가능하게 합니다.

다음은 HTML 및 CSS 코드 스니펫의 예입니다.

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
