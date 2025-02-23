# カウンター

VM 内には既に `index.html` と `style.css` が用意されています。

ネストされたリスト要素を考慮したカスタムなリストカウンターを作成するには、次の手順に従います。

1. `counter-reset` を使って、変数カウンターを初期化します（初期値は `0`）。名前は属性の値になります（例：`counter`）。
2. 各カウント可能な要素（例：各 `<li>`）に対して、変数カウンターに `counter-increment` を適用します。
3. 各カウント可能な要素（例：各 `<li>`）の `::before` 疑似要素の `content` の一部として、各変数カウンターの値を表示するために `counters()` を使います。渡される 2 番目の値（`'.'`）は、ネストされたカウンターの区切り文字として機能します。

以下は、HTML のコード例です。

```html
<ul>
  <li>List item</li>
  <li>List item</li>
  <li>
    List item
    <ul>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
  </li>
</ul>
```

そして、カスタムなリストカウンターを適用する CSS コードは以下の通りです。

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
