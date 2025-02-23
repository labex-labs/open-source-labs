# 接頭辞付き入力

VM内には既に`index.html`と`style.css`が用意されています。

可視的で編集不可の接頭辞付きの入力を作成するには、次の手順に従ってください。

1. `display: flex`を使用して、`.input-box`クラスのコンテナ要素を作成します。
2. `<input>`フィールドの境界線と輪郭を削除し、代わりに親要素に適用して入力ボックスのように見せます。
3. ユーザーが`<input>`フィールドとインタラクションする際に、`:focus-within`疑似クラスセレクタを使用して親要素をスタイリングします。

以下がHTMLコードです。

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

以下がCSSコードです。

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
