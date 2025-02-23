# 三角形

VM 内には既に `index.html` と `style.css` が用意されています。

CSS のみを使って三角形を作成するには、次の手順に従います。

1. 同じ `border-width`（`20px`）を持つ 3 つのボーダーを使って三角形を作成します。
2. 三角形が向いている側と反対側の `border-color` を目的の色に設定します。隣接するボーダーの `border-color` は `transparent` にする必要があります。
3. 三角形のサイズを調整するには、`border-width` の値を変更します。

以下はコードの例です。

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

右下隅の「Go Live」をクリックして 8080 ポートで Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
