# 空の要素を非表示にする

VM内には既に`index.html`と`style.css`が用意されています。

コンテンツがない要素を非表示にするには、`:empty`疑似クラスを使用します。たとえば、次のHTMLコードがある場合：

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

コンテンツがないボタン要素を非表示にするには、次のCSSコードを使用できます：

```css
p:empty {
  display: none;
}
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080**タブを更新してWebページをプレビューできます。
