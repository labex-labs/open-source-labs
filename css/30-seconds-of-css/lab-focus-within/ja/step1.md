# 子要素がフォーカスされたとき

VM には既に `index.html` と `style.css` が用意されています。

フォームの子要素のいずれかがフォーカスされたときにその外観を変更するには、疑似クラス `:focus-within` を使って親要素にスタイルを適用します。たとえば、与えられた HTML コードでは、入力フィールドのいずれかがフォーカスされると、`form` 要素の背景が緑になります。子要素にスタイルを適用するには、`label` や `input` などの適切な CSS セレクタを使います。

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブ ページをプレビューできます。
