# 段階的なアニメーション

VM 内には既に `index.html` と `style.css` が用意されています。

このコードは、リストの要素に対して段階的なアニメーションを作成します。そのためには以下のことを行います。

1. `opacity: 0` と `transform: translateX(100%)` を設定することで、リスト要素を透明にして最も右まで移動させます。
2. `transition-delay` を除き、リスト要素に同じ `transition` プロパティを指定します。
3. インラインスタイルを使って各リスト要素に `--i` の値を指定します。これは段階的な効果を作成するための `transition-delay` に使用されます。
4. チェックボックスに対して `:checked` 疑似クラスセレクタを使ってリスト要素をスタイリッシュにします。要素を表示させて表示領域にスライドさせるには、`opacity` を `1` に、`transform` を `translateX(0)` に設定します。

この効果を達成するための HTML と CSS のコードは以下の通りです。

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

右下隅の「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新して Web ページをプレビューできます。
