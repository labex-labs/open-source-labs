# 兄弟要素のフェード

VM内には既に`index.html`と`style.css`が用意されています。

ホバーした要素の兄弟要素をフェードアウトさせるには：

1. `transition`プロパティを使って`opacity`の変更をアニメーションさせます。

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. `:hover`と`:not`疑似クラスセレクタを使って、マウスが乗っていない要素以外のすべての要素の`opacity`を`0.5`に変更します。

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

以下はHTMLコードの例です：

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
