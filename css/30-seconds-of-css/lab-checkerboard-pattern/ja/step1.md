# チェッカーボードの背景パターン

`index.html` と `style.css` はすでに仮想マシン (VM) に用意されています。

チェッカーボードの背景パターンを作成するには、以下の手順に従ってください。

1. `background-color` プロパティを白に設定します。
2. `background-image` に 2 つの `linear-gradient()` 値を使用し、それぞれ異なる角度でチェッカーボードパターンを作成します。たとえば、一方の角度を `45deg`、もう一方を `-45deg` に設定します。
3. `background-size` を使用してパターンのサイズを指定します。たとえば、`60px 60px` とすると、60×60 ピクセルのパターンが作成されます。
4. `background-repeat` を使用してパターンの繰り返しを設定します。たとえば、`repeat` とすると、パターンが両方向に繰り返されます。
5. デモンストレーションのため、要素の `height` と `width` プロパティは 240px に固定されていることに注意してください。

以下は `.checkerboard` クラスを持つ HTML 要素の例です。

```html
<div class="checkerboard"></div>
```

対応する CSS は以下の通りです。

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

右下隅にある「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
