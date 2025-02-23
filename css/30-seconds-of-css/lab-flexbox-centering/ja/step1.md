# フレックスボックスの中央揃え

VM 内には既に `index.html` と `style.css` が用意されています。

親要素内の子要素をフレックスボックスを使って水平および垂直方向に中央揃えするには、次の手順に従います。

1. 親要素の `display` プロパティを `flex` に設定して、フレックスボックスレイアウトを作成します。
2. `justify-content` プロパティの値を `center` に設定して、子要素を水平方向に中央揃えします。
3. `align-items` プロパティの値を `center` に設定して、子要素を垂直方向に中央揃えします。
4. 親要素内に子要素を追加します。

以下はコードの例です。

```html
<div class="flexbox-centering">
  <div>Centered content.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
