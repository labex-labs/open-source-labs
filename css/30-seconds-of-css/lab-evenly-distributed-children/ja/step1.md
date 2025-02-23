# 子要素の均等配置

VM 内には既に `index.html` と `style.css` が用意されています。

親要素内の子要素を均等に配置するには、親要素の `display` プロパティを `flex` に設定してフレックスボックスレイアウトを使用します。子要素を水平方向に均等な間隔で配置するには、`justify-content: space-between` を使用します。子要素の周りに余白を持たせて配置するには、`justify-content: space-around` を使用します。以下は例です：

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
