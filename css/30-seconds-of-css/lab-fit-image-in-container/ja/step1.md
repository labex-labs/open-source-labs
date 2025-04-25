# コンテナ内に画像を収める

VM 内には既に `index.html` と `style.css` が用意されています。

画像のアスペクト比を維持しながら、その画像をコンテナ内に収めるには、`object-fit: contain` を使用します。画像のアスペクト比を維持しながらコンテナを埋めるには、`object-fit: cover` を使用します。画像をコンテナの中央に配置したい場合は、`object-position: center` を使用できます。

これらのプロパティを使用する方法の例を以下に示します。

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

そして対応する CSS：

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
