# 호버 시 이미지 회전

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

호버 시 이미지 회전 효과를 만들려면, `<figure>` 요소인 부모 요소 위에 마우스를 올릴 때 `scale()`, `rotate()`, 그리고 `transition` 속성을 사용하십시오. 이미지 변환이 부모 요소에서 넘치지 않도록 하려면 부모 요소의 CSS 에 `overflow: hidden`을 추가하십시오. 다음은 HTML 및 CSS 코드의 예입니다.

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
