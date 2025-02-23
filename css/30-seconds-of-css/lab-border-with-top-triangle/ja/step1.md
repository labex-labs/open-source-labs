# 上部に三角形を持つ境界

VM内には既に`index.html`と`style.css`が用意されています。

上部に三角形を持つコンテンツコンテナを作成するには、次の手順に従ってください。

1. `::before`と`::after`の疑似要素を使って2つの三角形を作成します。
2. 三角形の`border-color`と`background-color`をコンテナと一致させます。
3. 境界として機能するため、`::before`の三角形の`border-width`を`::after`の三角形より`1px`広く設定します。
4. 左の境界を表示するために、`::after`の三角形を`::before`の三角形の右に`1px`配置します。

コンテナの例となるHTMLコードは以下の通りです。

```html
<div class="container">Border with top triangle</div>
```

対応するCSSコードは以下の通りです。

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
