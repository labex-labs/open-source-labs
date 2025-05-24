# 등각 투영 카드 (Isometric Card)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

등각 투영 카드 (isometric card) 를 만들려면 `box-shadow`와 함께 `transform`을 사용하여 `rotateX()` 및 `rotateZ()`를 사용하십시오. 또한 사용자가 카드를 마우스로 가리킬 때 카드를 애니메이션하고 들어올리는 효과를 만들기 위해 `transition`을 추가할 수 있습니다.

다음은 코드 스니펫 (code snippet) 예시입니다.

```html
<div class="isometric-card"></div>
```

```css
.isometric-card {
  margin: 0 auto;
  transform: rotateX(51deg) rotateZ(43deg);
  transform-style: preserve-3d;
  background-color: #fcfcfc;
  will-change: transform;
  width: 240px;
  height: 320px;
  border-radius: 2rem;
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    28px 28px 28px 0 rgba(34, 33, 81, 0.25);
  transition:
    transform 0.4s ease-in-out,
    box-shadow 0.3s ease-in-out;
}

.isometric-card:hover {
  transform: translate3d(0px, -16px, 0px) rotateX(51deg) rotateZ(43deg);
  box-shadow:
    1px 1px 0 1px #f9f9fb,
    -1px 0 28px 0 rgba(34, 33, 81, 0.01),
    54px 54px 28px -10px rgba(34, 33, 81, 0.15);
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
