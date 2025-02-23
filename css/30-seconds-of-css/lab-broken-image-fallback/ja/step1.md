# 読み込みに失敗した画像の代替表示

VM内には既に`index.html`と`style.css`が用意されています。

画像の読み込みに失敗した場合、エラーメッセージをユーザーに表示します。これを行うには、`img`要素をテキストコンテナとしてスタイルを適用し、その表示をブロックに設定し、幅を100%に設定します。`::before`および`::after`疑似要素を使用して、それぞれエラーメッセージと画像のURLを表示します。これらの要素は、画像の読み込みに失敗した場合にのみ表示されます。

以下はコードの例です：

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
