# 画像の上にテキストを重ねる

VM 内には既に`index.html`と`style.css`が用意されています。

画像の上にオーバーレイをかけてテキストを表示するには、`backdrop-filter`プロパティを使って`blur(14px)`と`brightness(80%)`の効果を適用します。これにより、背景画像や色に関係なくテキストが読みやすくなります。以下は HTML コードの例です。

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

そして対応する CSS コードです。

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
