# ポップアウトメニュー

VM内には既に`index.html`と`style.css`が用意されています。

ホバー/フォーカス時にインタラクティブなポップアウトメニューを表示するには、次の手順に従ってください。

1. CSSで`left: 100%`を使用して、ポップアウトメニューを親要素の右に配置します。
2. ポップアウトメニューを最初は非表示にするには、`display: none`の代わりに`visibility: hidden`を使用して、トランジションを適用できるようにします。
3. 親要素に`:hover`、`:focus`、`:focus-within`の疑似クラスセレクタを適用して、ポップアウトメニューをホバー/フォーカス時に表示します。
4. 次のHTMLとCSSコードを使用してください。

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
