# 等角投影カード

VM には既に `index.html` と `style.css` が用意されています。

等角投影カードを作成するには、`rotateX()` と `rotateZ()` を使った `transform` と `box-shadow` を組み合わせます。また、`transition` を追加してカードをアニメーションさせ、ユーザーがカードの上にマウスオーバーしたときにリフトエフェクトを作成することもできます。

以下はコードの例です。

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

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
