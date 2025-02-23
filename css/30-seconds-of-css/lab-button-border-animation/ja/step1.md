# ボタンの枠線アニメーション

VM内には既に `index.html` と `style.css` が用意されています。

ホバー時に枠線をアニメーションさせるには、`::before` と `::after` 疑似要素を使って、横幅が `24px` でボックスの上下に配置される2つのボックスを生成します。そして、`:hover` 疑似クラスを適用して、ホバー時にそれら要素の `幅` を `100%` に増やし、`transition` を使って遷移をアニメーションさせます。

以下はコードの例です。

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

右下隅の「Go Live」をクリックして、ポート8080でWebサービスを実行してください。その後、**Web 8080** タブを更新してWebページをプレビューできます。
