# 3 タイルのレイアウト

VM 内には既に `index.html` と `style.css` が用意されています。

3 タイルのレイアウトを作成するには、`float`、`flex`、または `grid` の代わりに `display: inline-block` を使います。コンテナの幅を 3 列に均等に分割するために、`width` と `calc` を組み合わせて使います。空白を避けるために、`.tiles` の `font-size` を `0` に設定し、`<h2>` 要素の `font-size` を `20px` に設定してテキストを表示します。ブロック間の空白を解消するために `font-size: 0` を使う場合、相対単位（たとえば `em`）を使うと副作用が発生する場合があることに注意してください。

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
