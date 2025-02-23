# 無効な入力時の揺れ

VM には既に `index.html` と `style.css` が用意されています。

無効な入力があるときに揺れるアニメーションを作成するには、次の手順に従います。

1. 許可される入力を指定する正規表現を定義するために `pattern` 属性を使用します。たとえば、英字のみを許可するには `[A-Za-z]*` を使用します。
2. `@keyframes` を使用して揺れるアニメーションを定義します。入力を左右に移動させるために `margin-left` プロパティを設定します。
3. `:invalid` 疑似クラスを使用して、入力に揺れるアニメーションを適用します。
4. オプションとして、エラーを示すために入力に赤いボックスシャドウを追加します。

以下はコードの例です。

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
