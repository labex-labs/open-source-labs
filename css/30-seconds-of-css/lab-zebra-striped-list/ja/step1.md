# ゼブ模様のリスト

VM には既に `index.html` と `style.css` が用意されています。

交互の背景色を持つリストを作成するには、`:nth-child(odd)` または `:nth-child(even)` の疑似クラスセレクターを使用して、兄弟要素の中での位置に基づいて要素に異なる `background-color` を適用します。これは `<div>`、`<tr>`、`<p>`、`<ol>` などのさまざまな HTML 要素に適用できます。

`<li>` 要素で横並びのリストを作成する方法の例を以下に示します。

```html
<ul>
  <li>Item 01</li>
  <li>Item 02</li>
  <li>Item 03</li>
  <li>Item 04</li>
  <li>Item 05</li>
</ul>
```

```css
li:nth-child(odd) {
  background-color: #999;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
