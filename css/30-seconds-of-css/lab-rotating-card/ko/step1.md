# 회전하는 카드

`index.html` 및 `style.css`는 이미 VM 에 제공되었습니다.

마우스를 올렸을 때 회전하는 양면 카드를 만들려면 다음 단계를 따르세요.

1. 카드의 `backface-visibility`를 기본적으로 보이지 않도록 `none`으로 설정합니다.
2. 초기에는 카드의 뒷면에 `rotateY(-180deg)`를 설정하고, 카드의 앞면에 `rotateY(0deg)`를 설정합니다.
3. 마우스를 올리면 카드의 앞면에 `rotateY(180deg)`를 설정하고, 카드의 뒷면에 `rotateY(0deg)`를 설정합니다.
4. 회전 효과를 만들기 위해 적절한 `perspective` 값을 설정합니다.

다음은 HTML 및 CSS 코드의 예입니다.

```html
<div class="card">
  <div class="card-side front">
    <div>Front Side</div>
  </div>
  <div class="card-side back">
    <div>Back Side</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover .card-side.front {
  transform: rotateY(180deg);
}

.card:hover .card-side.back {
  transform: rotateY(0deg);
}
```

오른쪽 하단 모서리에 있는 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하세요. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
