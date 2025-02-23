# ボタンのフィルアニメーション

VM内には既に`index.html`と`style.css`が用意されています。

ホバー時のフィルアニメーションを作成するには、`color`と`background`プロパティを設定し、変更をアニメーション化するために適切な`transition`を適用します。ホバー時にアニメーションをトリガーするには、`:hover`疑似クラスを使って要素の`background`と`color`プロパティを変更します。以下はコードの例です：

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
