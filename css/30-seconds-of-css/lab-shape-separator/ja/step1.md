# 形状区切り線

VM 内には既に`index.html`と`style.css`が用意されています。

SVG 形状を使って 2 つの異なるブロック間に区切り線要素を作成するには、次の手順に従います。

1. `::after`疑似要素を使用します。
2. `background-image`プロパティを使ってデータ URI を通じて SVG 形状（24x12 の三角形）を追加します。背景画像はデフォルトで繰り返され、疑似要素の全域を覆います。
3. 親要素の`background`プロパティを使って区切り線に望ましい色を設定します。

次の HTML コードを使用します。

```html
<div class="shape-separator"></div>
```

そして次の CSS ルールを適用します。

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080**タブを更新して Web ページをプレビューできます。
