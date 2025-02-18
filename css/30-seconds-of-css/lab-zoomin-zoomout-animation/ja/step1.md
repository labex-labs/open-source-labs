# ズームイン・ズームアウトアニメーション

`index.html` と `style.css` はすでに仮想マシン (VM) に用意されています。

ズームイン・ズームアウトアニメーションを作成するには、以下の手順に従ってください。

1. `@keyframes` を使用して3段階のアニメーションを定義します。`0%` と `100%` では、`scale(1,1)` を使用して要素を元のサイズに設定します。`50%` では、`scale(1.5,1.5)` を使用して要素を元のサイズの1.5倍に拡大します。

2. `width` と `height` を使用して要素に特定のサイズを指定します。

3. `animation` を使用して要素に適切な値を設定し、アニメーションを実現します。

以下は HTML と CSS のコード例です。

```html
<div class="zoom-in-out-box"></div>
```

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}

@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

右下隅にある「Go Live」をクリックして、ポート 8080 でウェブサービスを起動してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
