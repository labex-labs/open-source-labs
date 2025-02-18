# ボタンの拡大アニメーション

`index.html` と `style.css` は、仮想マシン (VM) 内ですでに用意されています。

ホバー時に拡大アニメーションを作成するには、適切な `transition` を使用して要素の変更をアニメーション化することができます。`:hover` 疑似クラスを使用して、`transform` プロパティを `scale(1.1)` に変更します。これにより、ユーザーが要素の上にマウスを乗せたときに要素が拡大します。

以下は、使用できるコードの例です。

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

右下隅にある「Go Live」をクリックして、ポート 8080 でウェブサービスを起動してください。その後、**Web 8080** タブを更新すると、ウェブページをプレビューできます。
