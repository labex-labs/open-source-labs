# ボックスサイズのリセット

VM には既に `index.html` と `style.css` が用意されています。

要素の `幅` と `高さ` が `境界線` や `余白` の影響を受けないようにするには、`box-sizing: border-box` という CSS プロパティを使用します。これは、要素の `幅` と `高さ` の計算に `余白` と `境界線` を含みます。親要素から `ボックスサイズ` プロパティを継承したい場合は、`box-sizing: inherit` を使用します。

2 つの `div` 要素で `ボックスサイズ` プロパティを使用する例を以下に示します。

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

この例では、最初の `div` 要素は `box-sizing: border-box` で、2 番目の `div` 要素は `box-sizing: content-box` です。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
