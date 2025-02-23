# ナビゲーション リスト項目のホバーとフォーカス エフェクト

VM には既に `index.html` と `style.css` が用意されています。

ナビゲーション項目に独自のホバーとフォーカス エフェクトを作成するには、CSS 変換を次のように使用します。

1. リスト項目のアンカーに `::before` 疑似要素を使用してホバー エフェクトを作成します。`transform: scale(0)` を使用して非表示にします。
2. `:hover` と `:focus` 疑似クラスセレクタを使用して、疑似要素を `transform: scale(1)` に遷移させ、色付きの背景を表示します。
3. `z-index` を使用して、疑似要素がアンカー要素を覆わないようにします。

ナビゲーション メニューには、次の HTML コードを使用できます。

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

そして、次の CSS ルールを適用します。

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
