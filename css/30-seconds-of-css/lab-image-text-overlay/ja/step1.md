# オーバーレイテキスト付き画像

VM には既に `index.html` と `style.css` が用意されています。

オーバーレイテキスト付き画像を表示するには、`<figure>` 要素と `<figcaption>` 要素を使用します。CSS の `linear-gradient` プロパティを使って画像の上にオーバーレイ効果を作成します。以下はコードの例です。

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br />Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

右下隅の「Go Live」をクリックして 8080 ポートで Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
