# シフトするカード

VM には既に `index.html` と `style.css` が用意されています。

マウスオーバー時にシフトするカードを作成するには、次の手順に従います。

1. `.container` 要素に適切な `perspective` を設定して、シフト効果を可能にします。
2. `.card` 要素の `transform` プロパティに対して `transition` を追加します。
3. `Document.querySelector()` を使用して `.card` 要素を選択し、`mousemove` と `mouseout` イベントに対するイベントリスナーを追加します。
4. `Element.getBoundingClientRect()` を使用して、`.card` 要素の `x`、`y`、`width`、および `height` を取得します。
5. `x` 軸と `y` 軸に対して相対距離を `-1` と `1` の間の値として計算し、`transform` プロパティを通じて適用します。

ここにカードのサンプル HTML と CSS コードを示します。

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

.shifting-card.content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

そして、ホバー効果を追加する JavaScript コードをここに示します。

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

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
