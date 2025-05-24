# 카드 이동 (Shifting Card)

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

마우스를 올렸을 때 이동하는 카드를 만들려면 다음 단계를 따르세요:

1. 이동 효과를 허용하기 위해 `.container` 요소에 적절한 `perspective`를 설정합니다.
2. `.card` 요소의 `transform` 속성에 대한 `transition`을 추가합니다.
3. `Document.querySelector()`를 사용하여 `.card` 요소를 선택하고 `mousemove` 및 `mouseout` 이벤트에 대한 이벤트 리스너를 추가합니다.
4. `Element.getBoundingClientRect()`를 사용하여 `.card` 요소의 `x`, `y`, `width`, 그리고 `height`를 가져옵니다.
5. `x` 및 `y` 축에 대해 `-1`과 `1` 사이의 값으로 상대적인 거리를 계산하고 `transform` 속성을 통해 적용합니다.

다음은 카드를 위한 샘플 HTML 및 CSS 코드입니다:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Card</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card .content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

다음은 호버 효과를 추가하는 JavaScript 코드입니다:

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
