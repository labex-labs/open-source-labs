# ポーカドットの背景パターン

`index.html` と `style.css` はすでに仮想マシン（VM）に用意されています。

ポーカドットの背景パターンを作成するには、以下の手順に従ってください。

1. `background-color` プロパティを黒に設定します。
2. `background-image` プロパティに 2 つの `radial-gradient()` 値を使用して、2 つのドットを作成します。
3. `background-size` プロパティを使用してパターンのサイズを指定します。`background-position` を使用して 2 つのグラデーションを適切に配置します。
4. `background-repeat` を `repeat` に設定します。
5. 要素の固定された `height` と `width` は、デモンストレーション目的のみです。

以下は、クラス `polka-dot` を持つ div 要素の HTML コードの例です。

```html
<div class="polka-dot"></div>
```

そして、対応する CSS コードは次の通りです。

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

右下隅にある「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
