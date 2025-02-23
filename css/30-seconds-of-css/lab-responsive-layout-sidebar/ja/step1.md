# サイドバー付きのレスポンシブレイアウト

VM には既に `index.html` と `style.css` が用意されています。

コンテンツエリアとサイドバー付きのレスポンシブレイアウトを作成するには、親コンテナに `display: grid` を使用し、2 番目の列（サイドバー）に `minmax()` を使用して、それが `150px` から `20%` の間で領域を占めるようにし、1 番目の列（メインコンテンツ）に `1fr` を使用して残りの空間を占めるようにします。以下は、HTML と CSS のコードの例です。

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
