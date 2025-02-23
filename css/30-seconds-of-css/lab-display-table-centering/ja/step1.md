# テーブル表示による中央揃え

VM 内には既に `index.html` と `style.css` が用意されています。

子要素を親要素内で垂直方向と水平方向に中央揃えするには、次の手順に従います。

1. 固定された `height` と `width` を持つコンテナ要素を追加します。

```html
<div class="container"></div>
```

2. コンテナ要素の中に子要素を追加し、`.center` のクラスを付与します。

```html
  <div class="center"><span>Centered content</span></div>
</div>
```

3. CSS で、コンテナ要素に次のスタイルを適用します。

- `height` と `width` を望む固定値に設定します。
- ボーダーを追加します（任意）。

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. CSS で、子要素に次のスタイルを適用します。

- `.center` 要素を `<table>` 要素のように振る舞わせるために `display: table` を使用します。
- 要素が親要素内の利用可能なスペースを埋めるように `height` と `width` を `100%` に設定します。
- 子要素に `display: table-cell` を使用して、`<td>` 要素のように振る舞わせます。
- 子要素に `text-align: center` と `vertical-align: middle` を使用して、水平方向と垂直方向に中央揃えします。

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
