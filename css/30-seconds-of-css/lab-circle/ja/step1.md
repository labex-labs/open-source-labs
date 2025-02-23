# 円

VM内には既に`index.html`と`style.css`が用意されています。

CSSのみを使用して円形を作成するには、要素の境界を曲げるために`border-radius: 50%`プロパティを使用します。完全な円を保証するために、`width`と`height`の両方を同じ値に設定することを確認してください。異なる値を使用する場合、代わりに楕円が作成されます。以下はコードの例です：

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080**タブを更新してWebページをプレビューできます。
