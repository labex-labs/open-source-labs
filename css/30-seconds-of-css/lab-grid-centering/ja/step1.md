# グリッドの中央配置

VM内には既に`index.html`と`style.css`が用意されています。

親要素内の子要素を水平および垂直方向に中央配置するには、次の手順に従います。

1. `display: grid`を使ってグリッドレイアウトを作成します。
2. `justify-content: center`を使って子要素を水平方向に中央配置します。
3. `align-items: center`を使って子要素を垂直方向に中央配置します。

以下は、HTML構造の例です。

```html
<div class="parent">
  <div class="child">Centered content.</div>
</div>
```

そして、対応するCSSです。

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
