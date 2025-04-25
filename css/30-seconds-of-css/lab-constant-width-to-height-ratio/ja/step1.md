# 一定の幅高比

VM 内には既に`index.html`と`style.css`が用意されています。

このコードスニペットは、幅が変化する要素が比例した高さ値を維持するようにします。これを達成するには、`::before`疑似要素に`padding-top`を適用して、要素の高さを幅のパーセンテージに等しくします。高さと幅の比率は必要に応じて変更できます。たとえば、`padding-top`を`100%`にすると、1:1 の比率の応答性のある正方形が作成されます。このコードを使用するには、次の HTML コードを追加するだけです。

```html
<div class="constant-width-to-height-ratio"></div>
```

次に、次の CSS コードを追加します。

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
