# カスタムラジオボタン

VM には既に `index.html` と `style.css` が用意されています。

状態変更時にアニメーション付きのスタイリッシュなラジオボタンを作成するには、次の手順に従ってください。

1. `.radio-container` を作成し、フレックスボックスを使用してラジオボタンに適切なレイアウトを作成します。
2. `<input>` のスタイルをリセットし、それを使用してラジオボタンの輪郭と背景を作成します。
3. `::before` 要素を使用してラジオボタンの内側の円を作成します。
4. `transform: scale(1)` と CSS トランジションを使用して、状態変更時のアニメーション効果を作成します。

以下は、HTML のサンプル スニペットです。

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

そして、対応する CSS です。

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
