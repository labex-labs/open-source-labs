# ホバー時の下線アニメーション

VM内には既に `index.html` と `style.css` が用意されています。

ユーザーがテキストの上にホバーしたときにアニメーション付きの下線効果を作成するには、次の手順に従います。

1. `display: inline-block` を使用して、下線をテキストコンテンツの幅だけに広げます。
2. `::after` 疑似要素を使用して、`width: 100%` と `position: absolute` を設定して、コンテンツの下に配置します。
3. `transform: scaleX(0)` を使用して、初期状態で疑似要素を非表示にします。
4. `:hover` 疑似クラスセレクタを使用して、ホバー時に `transform: scaleX(1)` を適用して疑似要素を表示します。
5. `transform-origin: left` と適切な `transition` を使用して、`transform` をアニメーション化します。
6. 要素の中央から変換が始まるように、`transform-origin` プロパティを削除します。

ここに、テキスト要素にこの効果を適用するための例のHTMLコードがあります。

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

そして、対応するCSSコードはこちらです。

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
