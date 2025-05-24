# 이미지 텍스트 오버레이

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

이미지 위에 텍스트를 오버레이하여 표시하려면 `backdrop-filter` 속성을 사용하여 `blur(14px)` 및 `brightness(80%)` 효과를 적용하십시오. 이렇게 하면 배경 이미지와 색상에 관계없이 텍스트를 읽을 수 있습니다. 다음은 HTML 코드의 예입니다.

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

그리고 해당 CSS 코드입니다.

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
