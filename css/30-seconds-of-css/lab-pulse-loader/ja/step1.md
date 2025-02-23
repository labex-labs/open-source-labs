# パルスローダー

VM内には既に`index.html`と`style.css`が用意されています。

`animation-delay`プロパティを使ってパルスエフェクトのローダーアニメーションを作成するには、次の手順に従います。

1. `@keyframes`を使って2つの`<div>`要素に対するアニメーションを定義します。両方の要素の開始点（`0%`）では、`width`や`height`がなく、中央に配置されます。終了点（`100%`）では、両方の要素の`width`と`height`が増加し、`position`が`0`にリセットされます。
2. アニメーション時に`opacity`を`1`から`0`に遷移させ、`<div>`要素が拡大するときに消えるエフェクトを与えます。
3. 親コンテナ`.ripple-loader`に事前に定義された`width`と`height`を設定します。`position: relative`を使って子要素を配置します。
4. 2番目の`<div>`要素に`animation-delay`を使い、各要素が異なるタイミングでアニメーションを開始するようにします。

これを達成するためのHTMLとCSSコードは次の通りです。

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
