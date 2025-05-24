# 호버 시 원근 변환

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

요소에 호버 애니메이션과 함께 원근 변환을 생성하려면:

1. `transform` 속성을 `perspective()` 및 `rotateY()` 함수와 함께 사용하여 요소에 원근감을 적용합니다. 예를 들어, 왼쪽 원근감을 만들려면 `transform: perspective(1500px) rotateY(15deg);`를 사용합니다. 오른쪽 원근감을 만들려면 `transform: perspective(1500px) rotateY(-15deg);`를 사용합니다.

2. 요소에 호버 시 `transform` 속성에 애니메이션을 적용하려면 `transition` 속성을 사용합니다. 예를 들어, `transition: transform 1s ease 0s;`를 사용합니다.

3. 왼쪽에서 오른쪽으로 원근 효과를 미러링하려면, 오른쪽 원근감에서 `rotateY()` 값을 음수로 변경합니다. 예를 들어, `transform: perspective(1500px) rotateY(-15deg);`를 사용합니다.

예시 HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

예시 CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
