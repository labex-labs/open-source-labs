# テキストを省略する

VM には既に `index.html` と `style.css` が用意されています。

1 行より長いテキストを省略し、末尾に省略記号を追加するには、次の CSS プロパティを使用します。

- `overflow: hidden` で、テキストが要素の寸法を超えないようにする
- `white-space: nowrap` で、テキストが高さで 1 行を超えないようにする
- `text-overflow: ellipsis` で、テキストが要素の寸法を超えた場合に省略記号を追加する
- 省略記号を表示するタイミングを知るために、要素に固定の `width` を指定する

この方法は、単一行の要素にのみ適用されます。例えば：

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
