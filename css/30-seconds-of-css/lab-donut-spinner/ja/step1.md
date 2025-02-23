# ドーナツスピナー

VM には既に `index.html` と `style.css` が用意されています。

コンテンツの読み込みを示すために、要素全体に半透明の `border` を持つドーナツスピナーを作成します。ドーナツの読み込みインジケータとして機能するように、ある辺を除きます。そして、`transform: rotate()` を使って要素を回転させる適切なアニメーションを定義して使用します。以下は HTML と CSS のサンプルコードです。

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
