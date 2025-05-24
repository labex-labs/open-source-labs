# 사용자 정의 스크롤바

`index.html` 및 `style.css`는 이미 VM 에 제공되어 있습니다.

스크롤 가능한 오버플로우 (overflow) 가 있는 요소의 스크롤바 스타일을 사용자 정의하려면 `::-webkit-scrollbar`를 사용하여 스크롤바 요소의 스타일을 지정하고, `::-webkit-scrollbar-track`를 사용하여 스크롤바 트랙 (스크롤바의 배경) 의 스타일을 지정하며, `::-webkit-scrollbar-thumb`를 사용하여 스크롤바 썸 (드래그 가능한 요소) 의 스타일을 지정할 수 있습니다. 그러나 이 기술은 WebKit 기반 브라우저에서만 작동하며, 스크롤바 스타일 지정은 어떤 표준 트랙에도 포함되어 있지 않다는 점에 유의하십시오. 다음은 HTML 및 CSS 에서 이러한 선택자를 사용하는 예입니다.

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
