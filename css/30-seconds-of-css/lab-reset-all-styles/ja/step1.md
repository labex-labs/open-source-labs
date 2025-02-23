# すべてのスタイルをリセットする

VM には既に `index.html` と `style.css` が用意されています。

すべてのスタイルを初期値にリセットするには、`all` プロパティを使用します。このプロパティは `direction` と `unicode-bidi` プロパティには影響しません。その使用方法の例を以下に示します。

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
