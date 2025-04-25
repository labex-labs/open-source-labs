# アスペクト比

VM 内には既に `index.html` と `style.css` が用意されています。

このコードは、CSS のカスタムプロパティと `calc()` 関数を使って特定のアスペクト比のレスポンシブなコンテナを作成します。これを達成するには、次の手順に従います。

1. CSS のカスタムプロパティ `--aspect-ratio` を使って、望むアスペクト比を定義します。
2. コンテナ要素の `position` プロパティを `relative` に設定し、`height` プロパティを `0` に設定します。
3. `calc()` 関数と `--aspect-ratio` カスタムプロパティを使ってコンテナ要素の高さを計算し、それを `padding-bottom` プロパティとして設定します。
4. コンテナ要素の直下の子要素を `position: absolute`、`top: 0`、`left: 0`、`width: 100%`、`height: 100%` に設定します。
5. 子要素の `object-fit` プロパティを `cover` に設定することで、子要素のアスペクト比を維持します。

コンテナを作成するには、次の HTML と CSS コードを使用します。

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
