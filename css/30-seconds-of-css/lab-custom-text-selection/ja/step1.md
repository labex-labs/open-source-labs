# 選択されたテキストのカスタマイズ

VM には既に `index.html` と `style.css` が用意されています。

選択されたテキストのスタイルを変更するには、`::selection` 疑似セレクタを使用します。以下は、段落要素内のテキストを選択してスタイル付けするコードの例です。

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
