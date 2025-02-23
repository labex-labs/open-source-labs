# グラデーション テキスト

VM には既に `index.html` と `style.css` が用意されています。

テキストにグラデーション カラーを与えるには、CSS プロパティを使用できます。まず、`linear-gradient()` 値を持つ `background` プロパティを使用して、テキスト要素にグラデーション バックグラウンドを与えます。次に、`webkit-text-fill-color: transparent` を使用して、テキストを透明色で埋めます。最後に、`webkit-background-clip: text` を使用して、バックグラウンドをテキストでクリップし、グラデーション バックグラウンドを色としてテキストに埋めます。以下はコードの例です。

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
