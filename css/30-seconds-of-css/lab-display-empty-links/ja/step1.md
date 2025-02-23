# テキストのないリンクをスタイリッシュにする

VM には既に `index.html` と `style.css` が用意されています。

テキストのないリンクのリンク URL を表示するには、このようなリンクを選択するために `:empty` 疑似クラス、テキストのあるリンクを除外するために `:not` 疑似クラス、および `content` プロパティと `attr()` 関数を組み合わせて、リンク URL を `::before` 疑似要素に表示します。以下はコードの例です：

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
