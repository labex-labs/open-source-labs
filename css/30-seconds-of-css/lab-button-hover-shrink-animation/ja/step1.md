# ボタンの縮小アニメーション

VM 内には既に`index.html`と`style.css`が用意されています。

要素にマウスオーバー時の縮小アニメーションを作成するには、変更をアニメーション化するための適切な`transition`プロパティと、アニメーションをトリガーする`:hover`疑似クラスを使用できます。たとえば、ユーザーがクラス`button-shrink`のボタンの上にマウスオーバーしたときにそのボタンを縮小させたい場合、次の CSS を追加できます。

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

これにより、変更があるときにボタンのすべてのプロパティにトランジションエフェクトが適用され、ユーザーがボタンの上にマウスオーバーすると、ボタンが元のサイズの 80% に縮小します。ボタンの HTML コードは次のとおりです。

```html
<button class="button-shrink">Submit</button>
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
