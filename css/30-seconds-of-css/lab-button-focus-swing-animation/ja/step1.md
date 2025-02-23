# ボタンの揺れアニメーション

VM には既に `index.html` と `style.css` が用意されています。

フォーカス時に揺れるアニメーションを作成するには、要素の変更をアニメーション化するために適切な `transition` を使用します。次に、要素に `:focus` 疑似クラスを適用し、`transform` を使った `animation` を使って揺らすようにします。最後に、アニメーションを一度だけ再生するように `animation-iteration-count` を追加します。以下は、HTML と CSS でこれを行う方法の例です：

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
