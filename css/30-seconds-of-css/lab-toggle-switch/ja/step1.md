# トグルスイッチ

VM 内には既に `index.html` と `style.css` が用意されています。

以下に、もっと簡潔で明確な内容を示します。

CSS のみでトグルスイッチを作成するには、次の手順に従います。

1. `<label>` を `for` 属性を使ってチェックボックスの `<input>` 要素と関連付けます。
2. `<label>` の `::after` 疑似要素を使って、スイッチ用の円形のノブを作成します。
3. `:checked` 疑似クラスセレクタを使って、`transform: translateX(20px)` とスイッチの `background-color` を使ってノブの位置を変更します。
4. `position: absolute` と `left: -9999px` を使って `<input>` 要素を視覚的に非表示にします。

以下が HTML コードです。

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

以下が CSS コードです。

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
