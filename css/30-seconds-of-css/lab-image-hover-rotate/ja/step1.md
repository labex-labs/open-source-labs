# ホバー時に画像を回転させる

VM には既に `index.html` と `style.css` が用意されています。

親要素（`<figure>` 要素である必要があります）にホバーしたときに画像に回転エフェクトを作成するには、`scale()`、`rotate()`、および `transition` プロパティを使用します。画像の変換が親要素からはみ出さないようにするには、親要素の CSS に `overflow: hidden` を追加します。以下は、HTML と CSS のコードの例です。

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
