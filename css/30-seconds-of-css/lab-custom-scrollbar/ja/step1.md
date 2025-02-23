# カスタムなスクロールバー

VM内には既に `index.html` と `style.css` が用意されています。

スクロール可能なオーバーフローを持つ要素のスクロールバーのスタイルをカスタマイズするには、`::-webkit-scrollbar` を使ってスクロールバー要素のスタイルを設定し、`::-webkit-scrollbar-track` を使ってスクロールバーのトラック（スクロールバーの背景）のスタイルを設定し、`::-webkit-scrollbar-thumb` を使ってスクロールバーのサム（ドラッグ可能な要素）のスタイルを設定できます。ただし、この手法はWebKitベースのブラウザでのみ機能し、スクロールバーのスタイリングはいずれの標準トラックにも含まれていません。以下は、HTMLとCSSでこれらのセレクタを使用する方法の例です。

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
