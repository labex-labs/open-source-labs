# トランスフォームによる中央配置

VM 内には既に `index.html` と `style.css` が用意されています。

CSS トランスフォームを使って親要素内で子要素を垂直方向と水平方向に中央に配置するには、次の手順に従います。

1. 親要素の `position` プロパティを `relative` に設定し、子要素の `position` プロパティを `absolute` に設定して、親要素に対して相対的に配置します。
2. `left: 50%` と `top: 50%` を使って、子要素を親要素の左と上の端から 50% オフセットします。
3. `transform: translate(-50%, -50%)` を使ってその位置を打ち消し、垂直方向と水平方向に中央に配置します。
4. 親要素の固定された `height` と `width` は、示すためのものです。

以下は、HTML のコード例です。

```html
<div class="parent">
  <div class="child">Centered content</div>
</div>
```

そして、対応する CSS コードは次の通りです。

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
