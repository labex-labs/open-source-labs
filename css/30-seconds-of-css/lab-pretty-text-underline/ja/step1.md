# 美しいテキストの下線

VM内には既に`index.html`と`style.css`が用意されています。

下線を引いた文字が下線を切り取らないようにするには、`text-shadow`を4つの値で使用して、下線との交差部分を覆う太い影を作成します。`text-shadow`の色を`background`の色と一致させ、より大きなフォントに対して`px`値を調整します。`background-image`と`linear-gradient()`と`currentColor`を使って実際の下線を作成します。`background-position`、`background-repeat`、`background-size`を設定して、グラデーションを正しい位置に配置します。`::selection`疑似クラスセレクタを使って、テキストの影がテキスト選択を妨げないようにします。この効果は本来`text-decoration-skip-ink: auto`として実装されていますが、下線に対する制御が少ないことに注意してください。

以下はコードの例です。

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
